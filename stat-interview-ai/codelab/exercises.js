window.CODELAB = {
  "schemaVersion": 1,
  "note": "Answer keys are recomputed from the embedded data by tests/codelab_check.py. Do not edit an answer without updating the data.",
  "exercises": [
    {
      "id": "CL-001",
      "level": 2,
      "title": "MERGE without BY",
      "skill": "DATA step merge, IN= flags",
      "data": {
        "dm": [{"USUBJID":"01-001","AGE":63},{"USUBJID":"01-002","AGE":71},{"USUBJID":"01-003","AGE":58},{"USUBJID":"01-004","AGE":77}],
        "ex": [{"USUBJID":"01-001","EXTRT":"Placebo"},{"USUBJID":"01-002","EXTRT":"Xanomeline Low Dose"},{"USUBJID":"01-004","EXTRT":"Xanomeline High Dose"}]
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
      "explanation": "Without BY, SAS pairs row 3 of DM with row 3 of EX, and EX's USUBJID overwrites DM's. 01-003 silently becomes 01-004. With BY USUBJID and IF a, all 4 DM subjects are kept and only 01-003 (not dosed) has a missing EXTRT."
    },
    {
      "id": "CL-002",
      "level": 3,
      "title": "Treatment duration in ADSL",
      "skill": "ADaM date derivation",
      "data": {
        "adsl": [{"USUBJID":"01-701-1015","TRTSDT":"2014-01-02","TRTEDT":"2014-03-15"}]
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
      "explanation": "2014-03-15 minus 2014-01-02 is 72 days; counting both the first and last dose day gives 73. An off-by-one here propagates to exposure tables and compliance."
    },
    {
      "id": "CL-003",
      "level": 4,
      "title": "Independent QC with PROC COMPARE",
      "skill": "Double programming, PROC COMPARE",
      "data": {
        "prod": [{"USUBJID":"01-001","AGE":63,"SAFFL":"Y"},{"USUBJID":"01-002","AGE":71,"SAFFL":"Y"},{"USUBJID":"01-003","AGE":58,"SAFFL":"N"},{"USUBJID":"01-004","AGE":77,"SAFFL":"Y"},{"USUBJID":"01-005","AGE":66,"SAFFL":"Y"}],
        "qc":   [{"USUBJID":"01-005","AGE":66,"SAFFL":"Y"},{"USUBJID":"01-004","AGE":77,"SAFFL":"Y"},{"USUBJID":"01-003","AGE":58,"SAFFL":"Y"},{"USUBJID":"01-002","AGE":70,"SAFFL":"Y"},{"USUBJID":"01-001","AGE":63,"SAFFL":"Y"}]
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
      "explanation": "PROC COMPARE with an ID statement expects both datasets sorted by the ID variables. After sorting: 01-002 differs on AGE (71 vs 70) and 01-003 differs on SAFFL (N vs Y), so 2 subjects."
    }
  ]
};
