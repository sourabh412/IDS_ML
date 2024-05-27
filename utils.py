
MSG = "Denial of Service"

Label_dict = {0: 'back',
              1: 'buffer_overflow',
              2: 'ftp_write',
              3: 'guess_passwd',
              4: 'imap',
              5: 'ipsweep',
              6: 'land',
              7: 'loadmodule',
              8: 'multihop',
              9: 'neptune',
              10: 'nmap',
              11: 'normal',
              12: 'perl',
              13: 'phf',
              14: 'pod',
              15: 'portsweep',
              16: 'rootkit',
              17: 'satan',
              18: 'smurf',
              19: 'spy',
              20: 'teardrop',
              21: 'warezclient',
              22: 'warezmaster'}

Data = [[-0.1102492232124988, -0.0077622407405687, -0.0049186443837248,
        -0.0140888117606131, -0.089486422020401, -0.007735985028101,
        -0.0950756715255649, -0.0270228183568983, -0.8092618187059747,
        -0.01166364260376, -0.0366518691422586, -0.0244365072620093,
        -0.0123851503674033, -0.0261800241845427, -0.0186098963407359,
        -0.0412211975932753, 0.0, -0.002817493921369,
        -0.0975309439715147, 1.0557540418790106, -0.2166692203156777,
        -0.6372092679572258, -0.6319290328885425, 2.746402795083481,
        2.715364578035608, -1.366921731434956, -0.0169295977079487,
        -0.3745597044055346, 0.7343425609306344, -0.9363220430671004,
        -1.0496586099715604, -0.068553020255113, -0.4801968475158174,
        -0.2891034002628785, -0.6395319051152512, -0.6248707997445304,
        2.87440954782046, 2.753913722653446, False, True, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, True, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, True, False,
        False, False, False, False, False, False, False, False]]

Label = "normal"

Attack_time = 7

Model_path = "./Saved_models/KNN_classifier.pkl"

class Model:
    def predict(d):
        pass