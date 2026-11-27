"""Synthetic regression tests; no personal data or external connections."""
import math
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "03_MODELS"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jarvis_v333 as j

class Test333(unittest.TestCase):
    def test_01_version(self): self.assertEqual(j.VERSION, "3.33.0")
    def test_02_exact_whitespace(self): self.assertNotEqual(j.text_digest("a "), j.text_digest("a"))
    def test_03_unicode(self): self.assertEqual(j.TextRecord.preserve("café Ω", "s1").raw, "café Ω")
    def test_04_no_rewrite(self): self.assertEqual(j.TextRecord.preserve("raw", "s1", "edited").raw, "raw")
    def test_05_bad_hash(self):
        with self.assertRaises(ValueError): j.TextRecord("raw", "s1", "0"*64)
    def test_06_empty_source(self):
        with self.assertRaises(ValueError): j.TextRecord.preserve("raw", "")
    def test_07_same_video(self):
        self.assertEqual(j.video_id("https://youtu.be/AbCdEfGhI_0?si=one"), j.video_id("https://youtube.com/watch?v=AbCdEfGhI_0&si=two"))
    def test_08_bad_host(self):
        with self.assertRaises(ValueError): j.video_id("https://youtube.com.evil.example/watch?v=AbCdEfGhI_0")
    def test_09_bad_video(self):
        with self.assertRaises(ValueError): j.video_id("https://youtu.be/no")
    def test_10_local_clock(self): self.assertEqual(j.local_time("2026-01-31T14:00:57Z"), "2026-01-31T08:00:57-06:00")
    def test_11_unknown_timezone(self):
        with self.assertRaises(ValueError): j.parse_time("2026-01-31T14:00:57")
    def test_12_lag(self): self.assertEqual(j.lag_bounds("2026-01-01T00:00:00Z", "2026-01-01T00:00:01Z", .2, .3), (.5, 1.5))
    def test_13_negative_error(self):
        with self.assertRaises(ValueError): j.lag_bounds("2026-01-01T00:00:00Z", "2026-01-01T00:00:01Z", -1, 0)
    def test_14_latency(self): self.assertEqual(j.latency_ms(0, 12000000, "c1", "c1"), 12)
    def test_15_cross_clock(self):
        with self.assertRaises(ValueError): j.latency_ms(0, 1200, "c1", "c2")
    def test_16_reverse_clock(self):
        with self.assertRaises(ValueError): j.latency_ms(5, 4, "c1", "c1")
    def test_17_boolean_not_count(self):
        with self.assertRaises(ValueError): j.effective_n(True, 0)
    def test_18_nan(self):
        with self.assertRaises(ValueError): j.independent_family_chance(float("nan"), 10)
    def test_19_family_chance(self): self.assertAlmostEqual(j.independent_family_chance(.05, 100), .994079470779666)
    def test_20_zero_comparisons(self): self.assertEqual(j.independent_family_chance(.5, 0), 0)
    def test_21_certain_event(self): self.assertEqual(j.independent_family_chance(1, 3), 1)
    def test_22_neff_independent(self): self.assertEqual(j.effective_n(3, 0), 3)
    def test_23_neff_duplicate_limit(self): self.assertEqual(j.effective_n(3, 1), 1)
    def test_24_neff_partial(self): self.assertAlmostEqual(j.effective_n(10, .5), 1.8181818181818181)
    def test_25_holm(self): self.assertEqual(j.holm_adjust([.01, .04, .03]), [.03, .06, .06])
    def test_26_holm_empty(self): self.assertEqual(j.holm_adjust([]), [])
    def test_27_invalid_probability(self):
        with self.assertRaises(ValueError): j.holm_adjust([1.1])
    def test_28_required_trials(self): self.assertEqual(j.required_clean_trials(.0001), 29956)
    def test_29_rare_trials(self): self.assertEqual(j.required_clean_trials(.000001), 2995731)
    def test_30_upper_bound(self): self.assertLessEqual(j.zero_failure_upper(29956), .0001)
    def test_31_minimal_n(self): self.assertGreater(j.zero_failure_upper(29955), .0001)
    def test_32_graph_ablation(self): self.assertEqual([j.complete_graph_edges(n) for n in (12,13,14)], [66,78,91])
    def test_33_unitarity(self):
        a = j.evolve_diagonal([.5,-.5], [2**-.5,2**-.5], 12.3)
        self.assertAlmostEqual(sum(abs(z)**2 for z in a), 1)
    def test_34_invalid_state(self):
        with self.assertRaises(ValueError): j.evolve_diagonal([1], [2], 1)
    def test_35_time_zero(self): self.assertEqual(j.evolve_diagonal([1], [1], 0), [1+0j])
    def test_36_clock_probability(self):
        self.assertEqual(j.clock_conditioned_plus_probability(1,0), 1)
        self.assertAlmostEqual(j.clock_conditioned_plus_probability(1,math.pi), 0)
    def test_37_clock_agrees_with_schrodinger(self):
        t=.7; a=j.evolve_diagonal([.5,-.5], [2**-.5,2**-.5], t)
        self.assertAlmostEqual(abs(sum(a)/2**.5)**2,j.clock_conditioned_plus_probability(1,t))
    def test_38_no_receipt(self): self.assertFalse(j.validate_action_status("CONFIRMED", None))
    def test_39_receipt_reference(self): self.assertTrue(j.validate_action_status("CONFIRMED", "provider:synthetic"))
    def test_40_prepared_is_not_confirmed(self): self.assertTrue(j.validate_action_status("PREPARED", None))
    def test_41_invalid_status(self):
        with self.assertRaises(ValueError): j.validate_action_status("ENDORSED", "x")
    def test_42_invalid_hbar(self):
        with self.assertRaises(ValueError): j.evolve_diagonal([1], [1], 1, hbar=0)
    def test_43_duplicate_query_id(self):
        with self.assertRaises(ValueError): j.video_id("https://youtube.com/watch?v=AbCdEfGhI_0&v=AbCdEfGhI_1")
    def test_44_caption_unknown_not_translation(self):
        r=j.TextRecord.preserve("caption_uncertain", "machine_caption", "do not decode")
        self.assertEqual(r.source_id, "machine_caption")

if __name__ == "__main__": unittest.main()
