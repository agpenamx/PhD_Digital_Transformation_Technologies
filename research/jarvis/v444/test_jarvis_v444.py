"""Synthetic implementation checks, not clinical trials or external certification."""
import unittest, math, tempfile, wave, json
from pathlib import Path
import numpy as np
from jarvis_v444 import *

class Test444(unittest.TestCase):
 def tone(self,f=440,fs=8000):return .5*np.sin(2*np.pi*f*np.arange(fs)/fs)
 def test_01_version(self):self.assertEqual(VERSION,'4.44.0')
 def test_02_unicode(self):self.assertEqual(SourceRecord('s','user','CAFÉ','SELF_REPORT').raw,'CAFÉ')
 def test_03_whitespace_digest(self):self.assertNotEqual(SourceRecord('s','user','x ','SELF_REPORT').digest,SourceRecord('s','user','x','SELF_REPORT').digest)
 def test_04_warning_not_observation(self):self.assertEqual(observation_export([SourceRecord('s','assistant','if condition','QUOTED_WARNING')]),[])
 def test_05_quoted_user_warning_not_observation(self):self.assertEqual(observation_export([SourceRecord('s','user','if condition','QUOTED_WARNING')]),[])
 def test_06_self_report(self):self.assertEqual(len(observation_export([SourceRecord('s','user','sample observation','SELF_REPORT')])),1)
 def test_07_correction_preserves(self):
  r=SourceRecord('s','user','raw','SELF_REPORT');c=correction_event(r,'clarification','new message');self.assertEqual(r.raw,'raw');self.assertEqual(c['original_sha256'],r.digest)
 def test_08_missing_source(self):
  with self.assertRaises(ValueError):SourceRecord('','user','raw','SELF_REPORT')
 def test_09_unknown_kind(self):
  with self.assertRaises(ValueError):SourceRecord('s','user','raw','UNRECOGNIZED')
 def test_10_frequency(self):self.assertEqual(measure_samples(self.tone(),8000)['measurements'][0]['spectral_peak_hz'],440)
 def test_11_distinct_frequency(self):self.assertEqual(measure_samples(self.tone(480),8000)['measurements'][0]['spectral_peak_hz'],480)
 def test_12_rms(self):self.assertAlmostEqual(measure_samples(self.tone(),8000)['measurements'][0]['rms_fs'],.5/math.sqrt(2),places=10)
 def test_13_silence(self):
  m=measure_samples(np.zeros(80),8000)['measurements'][0];self.assertIsNone(m['spectral_peak_hz']);self.assertIsNone(m['rms_dbfs'])
 def test_14_stereo_no_phase_cancellation(self):
  x=self.tone();m=measure_samples(np.stack([x,-x],axis=1),8000);self.assertEqual([v['spectral_peak_hz'] for v in m['measurements']],[440,440])
 def test_15_no_calibrated_spl(self):self.assertIsNone(measure_samples(self.tone(),8000)['sound_pressure_level_db_spl'])
 def test_16_nan(self):
  with self.assertRaises(ValueError):measure_samples([float('nan')]*8,8000)
 def test_17_invalid_rate(self):
  with self.assertRaises(ValueError):measure_samples(self.tone(),True)
 def test_18_sample_range(self):
  with self.assertRaises(ValueError):measure_samples([2]*8,8000)
 def test_19_no_stereo_collapse(self):self.assertEqual(measure_samples(np.ones((8,2))*.1,8000)['channels'],2)
 def test_20_duration(self):self.assertEqual(measure_samples(self.tone(),8000)['duration_s'],1)
 def test_21_resolution(self):self.assertEqual(measure_samples(self.tone(),8000)['fft_bin_spacing_hz'],1)
 def test_22_wav_hash(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'synthetic.wav'
   with wave.open(str(p),'wb') as w:w.setparams((1,2,8000,0,'NONE','not compressed'));w.writeframes((self.tone()*32767).astype('<i2').tobytes())
   m=analyze_pcm16(p);self.assertEqual(len(m['source_sha256']),64);self.assertEqual(m['measurements'][0]['spectral_peak_hz'],440)
 def test_23_budget(self):self.assertEqual(scenario(20,750,2500,25000)['economic_cost_mxn'],'17500.00')
 def test_24_budget_not_debt(self):self.assertFalse(scenario(20,750,2500,25000)['receivable_verified'])
 def test_25_negative_budget(self):
  with self.assertRaises(ValueError):scenario(-1,1,1,1)
 def test_26_no_receipt(self):self.assertFalse(validate_delivery('SENT',None,True))
 def test_27_no_recipient_review(self):self.assertFalse(validate_delivery('SENT','provider-id',False))
 def test_28_prepared_not_sent(self):self.assertTrue(validate_delivery('PREPARED',None,False))
 def test_29_json_silence(self):json.dumps(measure_samples(np.zeros(8),8000),allow_nan=False)
 def test_30_mean_removed(self):self.assertIsNone(measure_samples(np.ones(8)*.5,8000)['measurements'][0]['spectral_peak_hz'])

if __name__=='__main__':unittest.main()
