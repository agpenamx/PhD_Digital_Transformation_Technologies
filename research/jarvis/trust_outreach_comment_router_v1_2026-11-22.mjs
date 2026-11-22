/** JARVIS Black Box consent & source-verified trust router v1.0
 * Pure, offline functions: NO network, email send, publishing, personal data collection or hiding comments.
 * Only user-authorized drafts; never infer authorizations from spiritual testimony.
 */
function classifyOutreach(x={}) {
  const v={ decision:"RESEARCH_ONLY",maxPrivilege:"PUBLIC_READ",sendAuthorized:false,reason:"Source verification or scoped permission required",humanReviewRequired:true };
  if(x.withdrawn||x.declined){return {...v,decision:"STOP",reason:"Recipient declined or withdrew consent"};}
  if(x.usesPrivateSocialGraph||x.indirectContactViaPrivateAssociate){return {...v,decision:"STOP",reason:"No profiling or backdoor contact through private individuals"};}
  if(x.claimsSpiritualOrMilitaryAuthority||x.catastropheVisionAsEvidence){return {...v,decision:"TESTIMONY_ONLY",reason:"Spiritual or catastrophic claim is not authenticated institutional authority"};}
  if(x.priorUnansweredCount>0&&!x.inboundExplicitInvitation){return {...v,decision:"STOP_FOLLOWUP",reason:"Prior unanswered outreach; do not bypass nonresponse"};}
  if(!x.sourceVerified){return v;}
  if(x.sensitivePersonalData||x.containsMedicalOrGeneticData){return {...v,decision:"CONFIDENTIAL_REVIEW",maxPrivilege:"PRIVATE_READ",reason:"Minimize or remove sensitive data; obtain specific consent"};}
  if(x.inboundExplicitInvitation&&x.recipientProfessionalRoleVerified){return {...v,decision:"DRAFT_FOR_REVIEW",maxPrivilege:"DRAFT_ONLY",reason:"Affirmative invitation supports a tailored reply, not automatic sending"};}
  if(x.verifiedPublicProfessionalChannel&&x.recipientProfessionalRoleVerified&&x.priorUnansweredCount===0){return {...v,decision:"DRAFT_FOR_REVIEW",maxPrivilege:"DRAFT_ONLY",reason:"First public professional inquiry may be drafted for case-by-case review"};}
  return v;
}

function planInterpretation(x={}){
  const audience=String(x.audience||"other"),language=x.recipientRequestedLanguage==="es"?"es":"en";
  const role=String(x.recipientPublicRole||"professional contact").slice(0,140);
  const topic=String(x.verifiedTopic||"JARVIS human-centered AI research").slice(0,160);
  return {
    audience,language,recipientRole:role,topic,
    sourceSignals:["recipient's own stated questions","public professional role","verified institutional remit"],
    claimLabels:["OBSERVED","HYPOTHESIS","PERSONAL_TESTIMONY","UNVERIFIED"],
    outline:language==="es"?["Motivo de contacto","Pregunta concreta","Evidencia verificable y límites","Invitación voluntaria sin presiones"]:
       ["Reason for contact","One clear question","Verified evidence and limitations","Optional invitation with an easy decline"],
    disclosure:language==="es"?"Proyecto independiente asistido por IA; sin respaldo institucional declarado.":
       "Independent AI-assisted research; no institutional endorsement claimed.",
    persuasionLimit:"No inferred religion, vulnerabilities, private likes, friend networks, psychological microtargeting or emotional pressure.",
    outputPermission:"DRAFT_ONLY; no send",
  };
}

function filterComment(x={}){
  if(!x.accountOwnedOrDelegated||!x.authorizedModerationScope)return {decision:"NO_ACCESS",actionTaken:false,reason:"No account/control permissions verified"};
  const s=String(x.text||"").slice(0,4000);
  if(/(?:i|we)\s+(?:will|am going to)\s+(?:kill|attack|hurt)\s+(?:you|them|him|her)\b/i.test(s) ||
     /(?:voy|vamos)\s+a\s+(?:matar|atacar)\b/i.test(s))
    return {decision:"FLAG_HUMAN_SAFETY_REVIEW",actionTaken:false,reason:"Possible direct threat; context and urgency must be reviewed"};
  if(/(?:buy followers|comprar seguidores|free crypto airdrop|send your password|env[ií]a tu contraseña)/i.test(s))
    return {decision:"FLAG_SPAM_REVIEW",actionTaken:false,reason:"Potential spam/fraud; verify before moderation"};
  if(/(?:leak your address|doxx?ing|i have your home address)/i.test(s))
    return {decision:"FLAG_PRIVACY_REVIEW",actionTaken:false,reason:"Possible privacy exposure; review before action"};
  return {decision:"ALLOW_OR_CONTEXT_REVIEW",actionTaken:false,reason:"Disagreement or spiritual critique is not grounds for suppression"};
}

export { classifyOutreach, planInterpretation, filterComment };
