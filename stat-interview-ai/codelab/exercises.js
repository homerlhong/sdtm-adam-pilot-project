window.CODELAB = {
 "schemaVersion": 1,
 "note": "Answer keys are recomputed from the embedded data by tests/codelab_check.py. Do not edit an answer without updating the data.",
 "exercises": [
  {
   "id": "OB-W1-01",
   "week": 1,
   "level": 1,
   "title": "Verbatim vs coded AE term",
   "skill": "SDTM AE structure",
   "data": {
    "ae": [
     {
      "USUBJID": "01-701-1015",
      "AETERM": "headache",
      "AEDECOD": "Headache"
     },
     {
      "USUBJID": "01-701-1015",
      "AETERM": "itchy skin at patch",
      "AEDECOD": "Application site pruritus"
     },
     {
      "USUBJID": "01-701-1023",
      "AETERM": "head ache",
      "AEDECOD": "Headache"
     },
     {
      "USUBJID": "01-701-1023",
      "AETERM": "red rash",
      "AEDECOD": "Erythema"
     },
     {
      "USUBJID": "01-701-1028",
      "AETERM": "HEADACHE",
      "AEDECOD": "Headache"
     }
    ]
   },
   "code": "proc freq data=ae;\n  tables aeterm;\nrun;",
   "bugQuestion": "The table should count subjects by preferred term. What is wrong?",
   "choices": [
    "PROC FREQ cannot count character variables",
    "It tabulates the verbatim AETERM instead of the coded AEDECOD",
    "AE must be merged with DM first",
    "AETERM should be upcased with a FORMAT"
   ],
   "bugAnswer": 1,
   "outputQuestion": "How many distinct subjects have the preferred term Headache?",
   "outputAnswer": 3,
   "explanation": "AETERM is what the investigator wrote, so 'headache', 'head ache' and 'HEADACHE' count as three different terms. AEDECOD is the MedDRA preferred term. Summaries use AEDECOD, which gives 3 subjects with Headache."
  },
  {
   "id": "OB-W1-02",
   "week": 1,
   "level": 2,
   "title": "DM must be one record per subject",
   "skill": "Domain structure, key checks",
   "data": {
    "dm": [
     {
      "USUBJID": "01-701-1015",
      "AGE": 63
     },
     {
      "USUBJID": "01-701-1023",
      "AGE": 64
     },
     {
      "USUBJID": "01-701-1023",
      "AGE": 64
     },
     {
      "USUBJID": "01-701-1028",
      "AGE": 71
     },
     {
      "USUBJID": "01-701-1033",
      "AGE": 74
     }
    ]
   },
   "code": "proc sort data=dm nodupkey;\n  by usubjid;\nrun;",
   "bugQuestion": "A colleague used this step to 'fix' DM. Why is it a problem?",
   "choices": [
    "NODUPKEY is not valid with BY",
    "It silently deletes the duplicate instead of reporting it for investigation",
    "It should sort by AGE",
    "Nothing; this is the standard fix"
   ],
   "bugAnswer": 1,
   "outputQuestion": "How many distinct subjects are in DM?",
   "outputAnswer": 4,
   "explanation": "DM is one record per subject. A duplicate USUBJID is a data issue to report and trace back to source. Deleting it with NODUPKEY hides the problem. Check keys with PROC SORT DUPOUT= or a COUNT(*) > 1 query. There are 4 distinct subjects."
  },
  {
   "id": "OB-W1-03",
   "week": 1,
   "level": 2,
   "title": "Partial ISO 8601 dates",
   "skill": "--DTC handling",
   "data": {
    "ae": [
     {
      "USUBJID": "01-701-1015",
      "AESTDTC": "2014-01-05"
     },
     {
      "USUBJID": "01-701-1015",
      "AESTDTC": "2014-03"
     },
     {
      "USUBJID": "01-701-1023",
      "AESTDTC": "2014-04-11"
     },
     {
      "USUBJID": "01-701-1028",
      "AESTDTC": "2014"
     }
    ]
   },
   "code": "data ae2;\n  set ae;\n  astdt = input(aestdtc, yymmdd10.);\n  format astdt date9.;\nrun;",
   "bugQuestion": "Why is this derivation not enough on its own?",
   "choices": [
    "YYMMDD10. cannot read hyphens",
    "Partial dates become missing and are lost without imputation or flagging per the SAP",
    "AESTDTC must be numeric",
    "FORMAT changes the stored value"
   ],
   "bugAnswer": 1,
   "outputQuestion": "How many records get a missing ASTDT from this code?",
   "outputAnswer": 2,
   "explanation": "Only complete YYYY-MM-DD values convert. '2014-03' and '2014' become missing. The SAP's partial-date rule (for example, impute the first day of the month, and set ASTDTF) must be applied. Otherwise TEAE flags can be wrong."
  },
  {
   "id": "OB-W2-01",
   "week": 2,
   "level": 3,
   "title": "Safety population flag",
   "skill": "ADSL population flags",
   "data": {
    "adsl": [
     {
      "USUBJID": "01-701-1015",
      "RANDFL": "Y",
      "DOSES": 84
     },
     {
      "USUBJID": "01-701-1023",
      "RANDFL": "Y",
      "DOSES": 0
     },
     {
      "USUBJID": "01-701-1028",
      "RANDFL": "Y",
      "DOSES": 30
     },
     {
      "USUBJID": "01-701-1033",
      "RANDFL": "N",
      "DOSES": 0
     },
     {
      "USUBJID": "01-701-1034",
      "RANDFL": "Y",
      "DOSES": 1
     }
    ]
   },
   "code": "data adsl;\n  set adsl;\n  if randfl = 'Y' then saffl = 'Y';\n  else saffl = 'N';\nrun;",
   "bugQuestion": "The SAP defines the safety population as subjects who received at least one dose. What is wrong?",
   "choices": [
    "SAFFL must be numeric",
    "It uses randomization instead of exposure, so a randomized but undosed subject is included",
    "ELSE is not allowed here",
    "SAFFL should come from DM.ARM"
   ],
   "bugAnswer": 1,
   "outputQuestion": "Per the SAP, how many subjects have SAFFL = 'Y'?",
   "outputAnswer": 3,
   "explanation": "01-701-1023 was randomized but never dosed. Safety is defined by exposure: DOSES >= 1 gives 3 subjects. The buggy code gives 4, so every safety table denominator would be wrong."
  },
  {
   "id": "OB-W2-02",
   "week": 2,
   "level": 3,
   "title": "Age group boundaries",
   "skill": "ADSL categorization",
   "data": {
    "adsl": [
     {
      "USUBJID": "01-701-1015",
      "AGE": 64
     },
     {
      "USUBJID": "01-701-1023",
      "AGE": 65
     },
     {
      "USUBJID": "01-701-1028",
      "AGE": 80
     },
     {
      "USUBJID": "01-701-1033",
      "AGE": 81
     },
     {
      "USUBJID": "01-701-1034",
      "AGE": 72
     }
    ]
   },
   "code": "data adsl;\n  set adsl;\n  length agegr1 $5;\n  if age < 65 then agegr1 = '<65';\n  else if age < 80 then agegr1 = '65-80';\n  else agegr1 = '>80';\nrun;",
   "bugQuestion": "The spec defines the groups as <65, 65-80 and >80. What is wrong?",
   "choices": [
    "LENGTH must come after SET",
    "The second condition should be AGE <= 80, so age 80 is misclassified",
    "Character values cannot contain '<'",
    "AGEGR1 should be numeric"
   ],
   "bugAnswer": 1,
   "outputQuestion": "Per the spec, how many subjects are in 65-80?",
   "outputAnswer": 3,
   "explanation": "The boundaries are inclusive: 65, 72 and 80 belong in 65-80, so 3 subjects. The code puts 80 in '>80'. Always test the exact boundary values."
  },
  {
   "id": "OB-W2-03",
   "week": 2,
   "level": 3,
   "title": "Baseline selection",
   "skill": "Baseline rules",
   "data": {
    "lb": [
     {
      "USUBJID": "01-701-1015",
      "ADT": "2013-12-20",
      "AVAL": 5.1
     },
     {
      "USUBJID": "01-701-1015",
      "ADT": "2013-12-30",
      "AVAL": ""
     },
     {
      "USUBJID": "01-701-1015",
      "ADT": "2014-01-02",
      "AVAL": 5.6
     },
     {
      "USUBJID": "01-701-1015",
      "ADT": "2014-01-20",
      "AVAL": 6.0
     }
    ],
    "adsl": [
     {
      "USUBJID": "01-701-1015",
      "TRTSDT": "2014-01-02"
     }
    ]
   },
   "code": "proc sort data=lb; by usubjid adt; run;\n\ndata base;\n  set lb;\n  by usubjid;\n  if first.usubjid;\n  base = aval;\nrun;",
   "bugQuestion": "The SAP says: baseline = last non-missing value on or before TRTSDT. What is wrong?",
   "choices": [
    "FIRST. requires NODUPKEY",
    "It takes the first record, not the last non-missing record on or before TRTSDT",
    "BY USUBJID should be BY ADT",
    "BASE must be character"
   ],
   "bugAnswer": 1,
   "outputQuestion": "What is the correct BASE value for 01-701-1015?",
   "outputAnswer": 5.6,
   "explanation": "Keep records with ADT <= TRTSDT and non-missing AVAL, then take the last one: 5.6 on 2014-01-02, the dosing day. The code returns 5.1. A wrong baseline shifts every CHG value."
  },
  {
   "id": "CL-001",
   "level": 2,
   "title": "MERGE without BY",
   "skill": "DATA step merge, IN= flags",
   "data": {
    "dm": [
     {
      "USUBJID": "01-001",
      "AGE": 63
     },
     {
      "USUBJID": "01-002",
      "AGE": 71
     },
     {
      "USUBJID": "01-003",
      "AGE": 58
     },
     {
      "USUBJID": "01-004",
      "AGE": 77
     }
    ],
    "ex": [
     {
      "USUBJID": "01-001",
      "EXTRT": "Placebo"
     },
     {
      "USUBJID": "01-002",
      "EXTRT": "Xanomeline Low Dose"
     },
     {
      "USUBJID": "01-004",
      "EXTRT": "Xanomeline High Dose"
     }
    ]
   },
   "code": "proc sort data=dm; by usubjid; run;\nproc sort data=ex; by usubjid; run;\n\ndata dm_ex;\n  merge dm(in=a) ex(in=b);\n  if a;\nrun;",
   "bugQuestion": "What is wrong with this program?",
   "choices": [
    "IN= flags cannot be used with MERGE",
    "The MERGE has no BY statement, so records are matched by position",
    "IF a; should be IF a and b;",
    "PROC SORT must use NODUPKEY"
   ],
   "bugAnswer": 1,
   "outputQuestion": "After adding BY USUBJID, how many records in DM_EX have a missing EXTRT?",
   "outputAnswer": 1,
   "explanation": "Without BY, SAS pairs row 3 of DM with row 3 of EX, and EX's USUBJID overwrites DM's. 01-003 silently becomes 01-004. With BY USUBJID and IF a, all 4 DM subjects are kept and only 01-003 (not dosed) has a missing EXTRT.",
   "week": 0
  },
  {
   "id": "CL-002",
   "level": 3,
   "title": "Treatment duration in ADSL",
   "skill": "ADaM date derivation",
   "data": {
    "adsl": [
     {
      "USUBJID": "01-701-1015",
      "TRTSDT": "2014-01-02",
      "TRTEDT": "2014-03-15"
     }
    ]
   },
   "code": "data adsl;\n  set adsl;\n  /* TRTSDT and TRTEDT are SAS numeric dates */\n  trtdurd = trtedt - trtsdt;\nrun;",
   "bugQuestion": "The spec says TRTDURD = TRTEDT - TRTSDT + 1 (both days counted). What is wrong?",
   "choices": [
    "Dates must be converted with INPUT() first",
    "The +1 is missing, so duration is one day short",
    "TRTDURD must be derived in ADEX, not ADSL",
    "Subtraction of SAS dates returns seconds"
   ],
   "bugAnswer": 1,
   "outputQuestion": "What is the correct TRTDURD for 01-701-1015?",
   "outputAnswer": 73,
   "explanation": "2014-03-15 minus 2014-01-02 is 72 days; counting both the first and last dose day gives 73. An off-by-one here propagates to exposure tables and compliance.",
   "week": 0
  },
  {
   "id": "CL-003",
   "level": 4,
   "title": "Independent QC with PROC COMPARE",
   "skill": "Double programming, PROC COMPARE",
   "data": {
    "prod": [
     {
      "USUBJID": "01-001",
      "AGE": 63,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-002",
      "AGE": 71,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-003",
      "AGE": 58,
      "SAFFL": "N"
     },
     {
      "USUBJID": "01-004",
      "AGE": 77,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-005",
      "AGE": 66,
      "SAFFL": "Y"
     }
    ],
    "qc": [
     {
      "USUBJID": "01-005",
      "AGE": 66,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-004",
      "AGE": 77,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-003",
      "AGE": 58,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-002",
      "AGE": 70,
      "SAFFL": "Y"
     },
     {
      "USUBJID": "01-001",
      "AGE": 63,
      "SAFFL": "Y"
     }
    ]
   },
   "code": "proc compare base=prod compare=qc listall;\n  id usubjid;\nrun;",
   "bugQuestion": "QC is stored in descending USUBJID order. What must happen before this COMPARE is valid?",
   "choices": [
    "Nothing; ID handles unsorted data",
    "Both datasets must be sorted by USUBJID",
    "LISTALL must be replaced by BRIEF",
    "QC must be created by copying production code"
   ],
   "bugAnswer": 1,
   "outputQuestion": "After sorting both datasets, how many subjects have at least one differing value?",
   "outputAnswer": 2,
   "explanation": "PROC COMPARE with an ID statement expects both datasets sorted by the ID variables. After sorting: 01-002 differs on AGE (71 vs 70) and 01-003 differs on SAFFL (N vs Y), so 2 subjects.",
   "week": 0
  }
 ],
 "weeks": {
  "1": "W1 · Data and standards",
  "2": "W2 · ADSL",
  "0": "Practice set"
 },
 "unlockPercent": 80
};
