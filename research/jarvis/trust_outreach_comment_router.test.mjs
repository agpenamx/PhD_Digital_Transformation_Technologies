/** No network; synthetic JARVIS trust-gate test suite. Run: node --test research/jarvis/trust_outreach_comment_router.test.mjs */
import test from "node:test";
import assert from "node:assert/strict";
import { classifyOutreach, planInterpretation, filterComment } from "./trust_outreach_comment_router_v1_2026-11-22.mjs";

test("private accounts remain unauthorized to route comments", () => {
  assert.equal(filterComment({ text:"Buy followers" }).decision,"NO_ACCESS");
});
test("respect repeated nonresponse", () => {
  assert.equal(classifyOutreach({sourceVerified:true,priorUnansweredCount:16,recipientProfessionalRoleVerified:true,verifiedPublicProfessionalChannel:true}).decision,"STOP_FOLLOWUP");
});
test("never contact through private associates", () => {
  assert.equal(classifyOutreach({usesPrivateSocialGraph:true}).decision,"STOP");
  assert.equal(classifyOutreach({indirectContactViaPrivateAssociate:true}).decision,"STOP");
});
test("declines/withdrawals take precedence over invitations", () => {
  assert.equal(classifyOutreach({declined:true,inboundExplicitInvitation:true}).decision,"STOP");
  assert.equal(classifyOutreach({withdrawn:true,inboundExplicitInvitation:true}).decision,"STOP");
});
test("spiritual and catastrophe language are not executable authorizations", () => {
  assert.equal(classifyOutreach({claimsSpiritualOrMilitaryAuthority:true}).decision,"TESTIMONY_ONLY");
  assert.equal(classifyOutreach({catastropheVisionAsEvidence:true}).sendAuthorized,false);
});
test("medical and DNA details cannot be placed into auto outreach", () => {
  assert.equal(classifyOutreach({sourceVerified:true,containsMedicalOrGeneticData:true}).decision,"CONFIDENTIAL_REVIEW");
});
test("unverified sources cannot be used for outreach", () => {
  assert.equal(classifyOutreach({sourceVerified:false,priorUnansweredCount:0}).decision,"RESEARCH_ONLY");
});
test("confirmed research invitation permits only draft", () => {
  let v=classifyOutreach({sourceVerified:true,inboundExplicitInvitation:true,recipientProfessionalRoleVerified:true});
  assert.equal(v.decision,"DRAFT_FOR_REVIEW");
  assert.equal(v.maxPrivilege,"DRAFT_ONLY");
  assert.equal(v.sendAuthorized,false);
});
test("first public channel permits only draft", () => {
  assert.equal(classifyOutreach({sourceVerified:true,verifiedPublicProfessionalChannel:true,recipientProfessionalRoleVerified:true,priorUnansweredCount:0}).maxPrivilege,"DRAFT_ONLY");
});
test("message personalization uses volunteered language", () => {
  const p=planInterpretation({recipientRequestedLanguage:"es",audience:"vatican_religious"});
  assert.equal(p.language,"es");
  assert.match(p.disclosure,/independiente/i);
});
test("no private microtargeting", () => {
  assert.match(planInterpretation({}).persuasionLimit,/No inferred religion/);
});
test("critical or skeptical comments are not removed", () => {
  let c=filterComment({accountOwnedOrDelegated:true,authorizedModerationScope:true,text:"I disagree with your spiritual explanation"});
  assert.equal(c.decision,"ALLOW_OR_CONTEXT_REVIEW");
  assert.equal(c.actionTaken,false);
});
test("threats flagged not automatically censored or sent", () => {
  let c=filterComment({accountOwnedOrDelegated:true,authorizedModerationScope:true,text:"I will kill you"});
  assert.equal(c.decision,"FLAG_HUMAN_SAFETY_REVIEW");
  assert.equal(c.actionTaken,false);
});
test("spam and privacy abuse flagged for human review", () => {
  assert.equal(filterComment({accountOwnedOrDelegated:true,authorizedModerationScope:true,text:"Buy followers"}).decision,"FLAG_SPAM_REVIEW");
  assert.equal(filterComment({accountOwnedOrDelegated:true,authorizedModerationScope:true,text:"I have your home address"}).decision,"FLAG_PRIVACY_REVIEW");
});
