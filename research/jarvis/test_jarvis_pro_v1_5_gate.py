"""Offline synthetic regression tests; no real contact identifiers."""
import unittest
from pathlib import Path
import importlib.util

P = Path(__file__).with_name("jarvis_pro_v1_5_gate.py")
spec = importlib.util.spec_from_file_location("jarvis_pro_gate", P)
gate = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = gate
spec.loader.exec_module(gate)

def fixture(**kwargs):
    args = dict(recipient_id="test-channel", authorized_exact_scope=True,
                reviewed_exact_message=True, reviewed_attachments=True,
                official_channel_verified=True)
    args.update(kwargs)
    return gate.DraftRequest(**args)

class TestPublicControls(unittest.TestCase):
    def test_seal_stable(self):
        self.assertEqual(gate.seal_verbatim("abc"), gate.seal_verbatim("abc"))
    def test_seal_changed(self):
        self.assertNotEqual(gate.seal_verbatim("abc"), gate.seal_verbatim("abd"))
    def test_class_invalid(self):
        with self.assertRaises(ValueError):
            gate.classify("CONFIRMED_BY_SPIRIT")
    def test_default_no_contact_authorization(self):
        self.assertEqual(gate.preflight(fixture(authorized_exact_scope=False)), "DRAFT_ONLY")
    def test_preflight_always_pending(self):
        self.assertEqual(gate.preflight(fixture()), "APPROVAL_PENDING")
    def test_decline(self):
        self.assertEqual(gate.preflight(fixture(consent="DECLINED")), "HOLD")
    def test_silence(self):
        self.assertEqual(gate.preflight(fixture(unanswered_previous=1)), "HOLD")
    def test_private_social_graph(self):
        self.assertEqual(gate.preflight(fixture(social_graph_targeting=True)), "HOLD")
    def test_sensitive_data(self):
        self.assertEqual(gate.preflight(fixture(sensitive_data=True)), "HOLD")
    def test_formal_channels(self):
        self.assertEqual(gate.preflight(fixture(formal_or_emergency=True)), "OFFICIAL_CHANNEL_REVIEW")
    def test_sent_is_not_delivered(self):
        result=gate.inspect_historical_messages([{"id":"s1","transport":"SENT","consent":"REQUESTED","assert_delivered":True}])
        self.assertFalse(result["passed"])
    def test_reply_is_not_agreement(self):
        result=gate.inspect_historical_messages([{"id":"s1","transport":"HUMAN_REPLY","consent":"REQUESTED","assert_agreed":True}])
        self.assertFalse(result["passed"])
    def test_duplicates(self):
        row={"id":"s1","transport":"DRAFT","consent":"NOT_REQUESTED"}
        self.assertFalse(gate.inspect_historical_messages([row,row])["passed"])
    def test_bad_chain(self):
        self.assertFalse(gate.check_chain([{"previous":"0"*64,"hash":"1"*64,"payload":{}}]))

if __name__ == "__main__":
    unittest.main()
