"""Synthetic deterministic unit checks; not a safety-validation dataset."""
import unittest
from hashlib import sha256
from trust_policy import assess_synthetic, apply_clarification, weighted_loss

class TrustPolicyTests(unittest.TestCase):
    def test_philosophical_mortality(self):
        self.assertEqual(assess_synthetic("When I eventually die, I hope love endures.").label, "mortality_philosophy")

    def test_spiritual_language_not_a_diagnosis(self):
        r = assess_synthetic("I believe my soul is eternal.")
        self.assertEqual(r.label, "mortality_philosophy")
        self.assertFalse(r.diagnosed)

    def test_ambiguous_phrase(self):
        self.assertEqual(assess_synthetic("When you no longer hear from me.").label, "ambiguous_request_clarification")

    def test_explicit_concern(self):
        self.assertEqual(assess_synthetic("I plan to kill myself tonight.").label, "acute_signal_for_review")

    def test_clarification_corrects(self):
        original="When you no longer hear from me."
        first=assess_synthetic(original)
        event=apply_clarification(original,first,"I mean human mortality; my soul is eternal.")
        self.assertEqual(event.first_assessment,"ambiguous_request_clarification")
        self.assertEqual(event.corrected_assessment,"mortality_philosophy")
        self.assertEqual(event.original_sha256,sha256(original.encode()).hexdigest())

    def test_new_explicit_signal_not_blocked_by_old_clarification(self):
        original="When you no longer hear from me."
        event=apply_clarification(original,assess_synthetic(original),"My soul is eternal.")
        self.assertEqual(event.corrected_assessment,"mortality_philosophy")
        self.assertEqual(assess_synthetic("I will end my life today.").label,"acute_signal_for_review")

    def test_nongeneralization(self):
        self.assertEqual(assess_synthetic("Unrelated ambiguous sentence.").label, "undetermined")

    def test_loss(self):
        self.assertAlmostEqual(weighted_loss(.1,.2,.3,.4), 1.7)

    def test_loss_rejects_bad_input(self):
        with self.assertRaises(ValueError): weighted_loss(-.1,0,0,0)

if __name__=="__main__":
    unittest.main()
