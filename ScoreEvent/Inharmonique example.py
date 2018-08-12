#!/usr/bin/env python
# encoding: utf-8

#Adapted from Risset's Inharmonique (1977)
#Csound version by Antonio de Sousa Dias

from pyo64 import *
from ScoreEvent import ScoreEvent

class Inharm:
    def __init__(self, duration, *args):
        self.trig = Trig()
        self.env = TrigEnv(self.trig, table, duration, mul=args[1])
        self.osc = Sine(freq=[args[0], args[0]], mul=self.env).out()


s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()
s.start()

table = ExpTable([(0, 0.00001), (800, 0.5), (3200, 0.05), (3360, 1), (4800, 0.1), (6080, 0.7), (6720, 0.05), (6880, 0.3), (7040, 0.05), (7360, 0.1), (8192, 0.00001)], exp=3)

score = ScoreEvent(s, globals())

score.addEvent(["Inharm",	0.5	,	2,	758.1662,	0.04923078	])
score.addEvent(["Inharm",	0.5	,	1.33335,	139.2779,	0.04923078])
score.addEvent(["Inharm",	0.5	,	1.83335,	388.6304,	0.04923078])
score.addEvent(["Inharm",	0.5	,	1.41665,	1244.5158,	0.04923078])
score.addEvent(["Inharm",	0.5	,	0.5,	1835.3238,	0.04923078	])
score.addEvent(["Inharm",	0.5	,	0.25,	2526.0974,	0.04923078	])
score.addEvent(["Inharm",	0.5	,	0.16665,	3303.3582,	0.04923078])
score.addEvent(["Inharm",	0.5	,	0.125,	4155.8739,	0.04923078	])
score.addEvent(["Inharm",	0.5	,	0.06665,	5058.9341,	0.04923078])
score.addEvent(["Inharm",	0.6	,	2,	400.3582,	0.04923078	])
score.addEvent(["Inharm",	0.6	,	1.33335,	73.5473,	0.04923078])
score.addEvent(["Inharm",	0.6	,	1.83335,	205.2206,	0.04923078])
score.addEvent(["Inharm",	0.6	,	1.41665,	657.1805,	0.04923078])
score.addEvent(["Inharm",	0.6	,	0.5,	969.1633,	0.04923078	])
score.addEvent(["Inharm",	0.6	,	0.25,	1333.9341,	0.04923078	])
score.addEvent(["Inharm",	0.6	,	0.16665,	1744.3754,	0.04923078])
score.addEvent(["Inharm",	0.6	,	0.125,	2194.5559,	0.04923078	])
score.addEvent(["Inharm",	0.6	,	0.06665,	2671.4269,	0.04923078])
score.addEvent(["Inharm",	0.7	,	2,	862.6074,	0.04923078	])
score.addEvent(["Inharm",	0.7	,	1.33335,	158.4642,	0.04923078])
score.addEvent(["Inharm",	0.7	,	1.83335,	442.1662,	0.04923078])
score.addEvent(["Inharm",	0.7	,	1.41665,	1415.9542,	0.04923078])
score.addEvent(["Inharm",	0.7	,	0.5,	2088.149,	0.04923078	])
score.addEvent(["Inharm",	0.7	,	0.25,	2874.0802,	0.04923078	])
score.addEvent(["Inharm",	0.7	,	0.16665,	3758.4126,	0.04923078])
score.addEvent(["Inharm",	0.7	,	0.125,	4728.3668,	0.04923078	])
score.addEvent(["Inharm",	0.7	,	0.06665,	5755.8281,	0.04923078])
score.addEvent(["Inharm",	0.775	,	20.17165,	231.017,	0.10650888	])
score.addEvent(["Inharm",	0.775	,	18.1545,	230.5213,	0.06390534	])
score.addEvent(["Inharm",	0.775	,	15.12875,	308.3532,	0.06390534	])
score.addEvent(["Inharm",	0.775	,	14.12015,	309.3447,	0.0213018	])
score.addEvent(["Inharm",	0.775	,	10.08585,	388.6638,	0.04260354	])
score.addEvent(["Inharm",	0.775	,	7.0601,	462.5298,	0.08520708	])
score.addEvent(["Inharm",	0.775	,	7.0601,	467.4872,	0.04260354	])
score.addEvent(["Inharm",	0.775	,	4.03435,	549.2851,	0.04260354	])
score.addEvent(["Inharm",	0.775	,	3.02575,	653.3915,	0.0213018	])
score.addEvent(["Inharm",	0.775	,	2.01715,	776.3362,	0.03195264	])
score.addEvent(["Inharm",	0.775	,	2.52145,	872.5106,	0.04260354	])
score.addEvent(["Inharm",	5.5	,	7.132,	653.3915,	0.03550296	])
score.addEvent(["Inharm",	5.5	,	6.4188,	651.9894,	0.0213018	])
score.addEvent(["Inharm",	5.5	,	5.349,	872.1234,	0.0213018	])
score.addEvent(["Inharm",	5.5	,	4.9924,	874.9277,	0.00710058	])
score.addEvent(["Inharm",	5.5	,	3.566,	1099.2681,	0.01420116	])
score.addEvent(["Inharm",	5.5	,	2.4962,	1308.1851,	0.02840238	])
score.addEvent(["Inharm",	5.5	,	2.4962,	1322.2064,	0.01420116	])
score.addEvent(["Inharm",	5.5	,	1.4264,	1553.5574,	0.01420116	])
score.addEvent(["Inharm",	5.5	,	1.0698,	1848.0043,	0.00710058	])
score.addEvent(["Inharm",	5.5	,	0.7132,	2195.7319,	0.0106509	])
score.addEvent(["Inharm",	5.5	,	0.8915,	2467.7447,	0.01420116	])
score.addEvent(["Inharm",	6.25	,	6.35135,	733.7021,	0.03550296	])
score.addEvent(["Inharm",	6.25	,	5.7162,	732.1277,	0.0213018	])
score.addEvent(["Inharm",	6.25	,	4.7635,	979.3191,	0.0213018	])
score.addEvent(["Inharm",	6.25	,	4.44595,	982.4681,	0.00710058	])
score.addEvent(["Inharm",	6.25	,	3.1757,	1234.383,	0.01420116	])
score.addEvent(["Inharm",	6.25	,	2.22295,	1468.9787,	0.02840238	])
score.addEvent(["Inharm",	6.25	,	2.22295,	1484.7234,	0.01420116	])
score.addEvent(["Inharm",	6.25	,	1.27025,	1744.5106,	0.01420116	])
score.addEvent(["Inharm",	6.25	,	0.9527,	2075.1489,	0.00710058	])
score.addEvent(["Inharm",	6.25	,	0.63515,	2465.617,	0.0106509	])
score.addEvent(["Inharm",	6.25	,	0.7939,	2771.0638,	0.01420116	])
score.addEvent(["Inharm",	10.25	,	10.08585,	462.034,	0.03550296	])
score.addEvent(["Inharm",	10.25	,	9.07725,	461.0426,	0.0213018	])
score.addEvent(["Inharm",	10.25	,	7.5644,	616.7064,	0.0213018	])
score.addEvent(["Inharm",	10.25	,	7.0601,	618.6894,	0.00710058	])
score.addEvent(["Inharm",	10.25	,	5.0429,	777.3277,	0.01420116	])
score.addEvent(["Inharm",	10.25	,	3.53005,	925.0596,	0.02840238	])
score.addEvent(["Inharm",	10.25	,	3.53005,	934.9745,	0.01420116	])
score.addEvent(["Inharm",	10.25	,	2.01715,	1098.5702,	0.01420116	])
score.addEvent(["Inharm",	10.25	,	1.5129,	1306.783,	0.00710058	])
score.addEvent(["Inharm",	10.25	,	1.0086,	1552.6723,	0.0106509	])
score.addEvent(["Inharm",	10.25	,	1.26075,	1745.0213,	0.01420116	])
score.addEvent(["Inharm",	17.5	,	10.6818,	436.2553,	0.0887574	])
score.addEvent(["Inharm",	17.5	,	9.61365,	435.3191,	0.05325444	])
score.addEvent(["Inharm",	17.5	,	8.01135,	582.2979,	0.05325444	])
score.addEvent(["Inharm",	17.5	,	7.47725,	584.1702,	0.01775148	])
score.addEvent(["Inharm",	17.5	,	5.3409,	733.9574,	0.03550296	])
score.addEvent(["Inharm",	17.5	,	3.73865,	873.4468,	0.07100592	])
score.addEvent(["Inharm",	17.5	,	3.73865,	882.8085,	0.03550296	])
score.addEvent(["Inharm",	17.5	,	2.13635,	1037.2766,	0.03550296	])
score.addEvent(["Inharm",	17.5	,	1.60225,	1233.8723,	0.01775148	])
score.addEvent(["Inharm",	17.5	,	1.0682,	1466.0426,	0.02662722	])
score.addEvent(["Inharm",	17.5	,	1.33525,	1647.6596,	0.03550296	])
score.addEvent(["Inharm",	4	,	19.91435,	232.9978,	0.05625	])
score.addEvent(["Inharm",	4	,	15.9315,	232.5961,	0.03375	])
score.addEvent(["Inharm",	4	,	14.93575,	303.8011,	0.03375	])
score.addEvent(	["Inharm",	4	,	10.9529,	304.8054,	0.01125	])
score.addEvent(	["Inharm",	4	,	9.95715,	389.1667,	0.0225	])
score.addEvent(	["Inharm",	4	,	6.97,	468.5065,	0.045	])
score.addEvent(	["Inharm",	4	,	4.9786,	473.528,	0.0225	])
score.addEvent(	["Inharm",	4	,	3.98285,	542.3226,	0.0225	])
score.addEvent(	["Inharm",	4	,	2.98715,	622.6667,	0.01125	])
score.addEvent(	["Inharm",	4	,	2.4893,	783.3548,	0.016875	])
score.addEvent(	["Inharm",	4	,	2.98715,	863.6989,	0.0225	])
score.addEvent(	["Inharm",	6	,	10.5682,	439.0538,	0.0375	])
score.addEvent(	["Inharm",	6	,	8.45455,	438.2968,	0.0225	])
score.addEvent(	["Inharm",	6	,	7.92615,	572.4731,	0.0225	])
score.addEvent(	["Inharm",	6	,	5.8125,	574.3656,	0.0075	])
score.addEvent(	["Inharm",	6	,	5.2841,	733.3333,	0.015	])
score.addEvent(	["Inharm",	6	,	3.69885,	882.8387,	0.03	])
score.addEvent(	["Inharm",	6	,	2.64205,	892.3011,	0.015	])
score.addEvent(	["Inharm",	6	,	2.11365,	1021.9355,	0.015	])
score.addEvent(	["Inharm",	6	,	1.58525,	1173.3333,	0.0075	])
score.addEvent(	["Inharm",	6	,	1.321,	1476.129,	0.01125	])
score.addEvent(	["Inharm",	6	,	1.58525,	1627.5269,	0.015	])
score.addEvent(	["Inharm",	10.6	,	9.97855,	464.9978,	0.01875	])
score.addEvent(	["Inharm",	10.6	,	7.98285,	464.1961,	0.01125	])
score.addEvent(	["Inharm",	10.6	,	7.4839,	606.3011,	0.01125	])
score.addEvent(	["Inharm",	10.6	,	5.4882,	608.3054,	0.00375	])
score.addEvent(	["Inharm",	10.6	,	4.98925,	776.6667,	0.0075	])
score.addEvent(	["Inharm",	10.6	,	3.4925,	935.0065,	0.015	])
score.addEvent(	["Inharm",	10.6	,	2.49465,	945.028,	0.0075	])
score.addEvent(	["Inharm",	10.6	,	1.9957,	1082.3226,	0.0075	])
score.addEvent(	["Inharm",	10.6	,	1.4968,	1242.6667,	0.00375	])
score.addEvent(	["Inharm",	10.6	,	1.2473,	1563.3548,	0.005625	])
score.addEvent(	["Inharm",	10.6	,	1.4968,	1723.6989,	0.0075	])
score.addEvent(	["Inharm",	17.51	,	5.2781,	879.1054,	0.09375	])
score.addEvent(	["Inharm",	17.51	,	4.22245,	877.5897,	0.05625	])
score.addEvent(	["Inharm",	17.51	,	3.95855,	1146.2473,	0.05625	])
score.addEvent(	["Inharm",	17.51	,	2.90295,	1150.0366,	0.01875	])
score.addEvent(	["Inharm",	17.51	,	2.63905,	1468.3333,	0.0375	])
score.addEvent(	["Inharm",	17.51	,	1.84735,	1767.6839,	0.075	])
score.addEvent(	["Inharm",	17.51	,	1.3195,	1786.6301,	0.0375	])
score.addEvent(	["Inharm",	17.51	,	1.0556,	2046.1935,	0.0375	])
score.addEvent(	["Inharm",	17.51	,	0.7917,	2349.3333,	0.01875	])
score.addEvent(	["Inharm",	17.51	,	0.65975,	2955.6129,	0.028125	])
score.addEvent(	["Inharm",	17.51	,	0.7917,	3258.7527,	0.0375	])
score.addEvent(	["Inharm",	7	,	5.3243,	225.3807,	0.12	])
score.addEvent(	["Inharm",	7	,	5.0581,	260.1269,	0.10000002	])
score.addEvent(	["Inharm",	7	,	4.5257,	361.5482,	0.12	])
score.addEvent(	["Inharm",	7	,	2.66215,	568.1472,	0.07999998	])
score.addEvent(	["Inharm",	7	,	3.72705,	93.9086,	0.04000002	])
score.addEvent(	["Inharm",	7	,	2.9284,	629.1878,	0.04000002	])
score.addEvent(	["Inharm",	7	,	2.12975,	762.5381,	0.04000002	])
score.addEvent(	["Inharm",	9.5	,	12.5639,	57.7051,	0.036	])
score.addEvent(	["Inharm",	9.5	,	11.0562,	61.6847,	0.027	])
score.addEvent(	["Inharm",	9.5	,	10.0511,	101.4814,	0.018	])
score.addEvent(	["Inharm",	9.5	,	12.5639,	291.5102,	0.108	])
score.addEvent(	["Inharm",	9.5	,	10.0511,	292.0076,	0.036	])
score.addEvent(	["Inharm",	9.5	,	8.54345,	347.2254,	0.072	])
score.addEvent(	["Inharm",	9.5	,	7.53835,	345.2356,	0.054	])
score.addEvent(	["Inharm",	9.5	,	6.5332,	437.7627,	0.036	])
score.addEvent(	["Inharm",	9.5	,	5.5281,	580.0356,	0.018	])
score.addEvent(	["Inharm",	9.5	,	2.5128,	666.5932,	0.018	])
score.addEvent(	["Inharm",	9.5	,	1.50765,	925.2712,	0.054	])
score.addEvent(	["Inharm",	12	,	10.27275,	218.0531,	0.06428574	])
score.addEvent(	["Inharm",	12	,	9.24545,	219.0265,	0.04285716	])
score.addEvent(	["Inharm",	12	,	6.67725,	358.2301,	0.06428574	])
score.addEvent(	["Inharm",	12	,	5.65,	359.885,	0.11571426	])
score.addEvent(	["Inharm",	12	,	3.33865,	463.3628,	0.17142858	])
score.addEvent(	["Inharm",	12	,	3.59545,	661.9469,	0.10714284	])
score.addEvent(	["Inharm",	12	,	2.5682,	778.7611,	0.09428574	])
score.addEvent(	["Inharm",	12	,	2.05455,	1064.9558,	0.08571426	])
score.addEvent(	["Inharm",	12	,	1.5409,	1168.1416,	0.08571426	])
score.addEvent(	["Inharm",	12	,	1.02725,	1464.0708,	0.06428574	])
score.addEvent(	["Inharm",	12	,	0.77045,	1584.7788,	0.08571426	])
score.addEvent(	["Inharm",	13.5	,	4.0794,	549.0973,	0.01928574	])
score.addEvent(	["Inharm",	13.5	,	3.6715,	551.5487,	0.01285716	])
score.addEvent(	["Inharm",	13.5	,	2.6516,	902.0885,	0.01928574	])
score.addEvent(	["Inharm",	13.5	,	2.2437,	906.2558,	0.03471426	])
score.addEvent(	["Inharm",	13.5	,	1.3258,	1166.8319,	0.05142858	])
score.addEvent(	["Inharm",	13.5	,	1.4278,	1666.9027,	0.03214284	])
score.addEvent(	["Inharm",	13.5	,	1.01985,	1961.0619,	0.02828574	])
score.addEvent(	["Inharm",	13.5	,	0.8159,	2681.7522,	0.02571426	])
score.addEvent(	["Inharm",	13.5	,	0.6119,	2941.5929,	0.02571426	])
score.addEvent(	["Inharm",	13.5	,	0.40795,	3686.7965,	0.01928574	])
score.addEvent(	["Inharm",	13.5	,	0.30595,	3990.7611,	0.02571426	])
score.addEvent(	["Inharm",	13.65	,	2.4625,	487.3096,	0.04000002	])
score.addEvent(	["Inharm",	13.65	,	2.33935,	562.4365,	0.03333336	])
score.addEvent(	["Inharm",	13.65	,	2.09315,	781.7259,	0.04000002	])
score.addEvent(	["Inharm",	13.65	,	1.23125,	1228.4264,	0.02666664	])
score.addEvent(	["Inharm",	13.65	,	1.72375,	203.0457,	0.01333332	])
score.addEvent(	["Inharm",	13.65	,	1.35435,	1360.4061,	0.01333332	])
score.addEvent(	["Inharm",	13.65	,	0.985,	1648.731,	0.01333332	])
score.addEvent(	["Inharm",	17.545	,	13.31225,	54.461,	0.048	])
score.addEvent(	["Inharm",	17.545	,	11.7148,	58.2169,	0.036	])
score.addEvent(	["Inharm",	17.545	,	10.6498,	95.7763,	0.024	])
score.addEvent(	["Inharm",	17.545	,	13.31225,	275.122,	0.144	])
score.addEvent(	["Inharm",	17.545	,	10.6498,	275.5915,	0.048	])
score.addEvent(	["Inharm",	17.545	,	9.05235,	327.7051,	0.096	])
score.addEvent(	["Inharm",	17.545	,	7.98735,	325.8271,	0.072	])
score.addEvent(	["Inharm",	17.545	,	6.9224,	413.1525,	0.048	])
score.addEvent(	["Inharm",	17.545	,	5.8574,	547.4271,	0.024	])
score.addEvent(	["Inharm",	17.545	,	2.66245,	629.1186,	0.024	])
score.addEvent(	["Inharm",	17.545	,	1.59745,	873.2542,	0.072	])
score.addEvent(	["Inharm",	25	,	12.5639,	57.7051,	0.072	])
score.addEvent(	["Inharm",	25	,	11.0562,	61.6847,	0.054	])
score.addEvent(	["Inharm",	25	,	10.0511,	101.4814,	0.036	])
score.addEvent(	["Inharm",	25	,	12.5639,	291.5102,	0.216	])
score.addEvent(	["Inharm",	25	,	10.0511,	292.0076,	0.072	])
score.addEvent(	["Inharm",	25	,	8.54345,	347.2254,	0.144	])
score.addEvent(	["Inharm",	25	,	7.53835,	345.2356,	0.108	])
score.addEvent(	["Inharm",	25	,	6.5332,	437.7627,	0.072	])
score.addEvent(	["Inharm",	25	,	5.5281,	580.0356,	0.036	])
score.addEvent(	["Inharm",	25	,	2.5128,	666.5932,	0.036	])
score.addEvent(	["Inharm",	25	,	1.50765,	925.2712,	0.108	])
score.addEvent(	["Inharm",	21	,	6.3642,	137.6452,	0.10546872	])
score.addEvent(	["Inharm",	21	,	5.83385,	195.1545,	0.0703125	])
score.addEvent(	["Inharm",	21	,	4.2428,	261.1488,	0.0703125	])
score.addEvent(	["Inharm",	21	,	5.3035,	310.833,	0.05273436	])
score.addEvent(	["Inharm",	21	,	3.1821,	439.3333,	0.05273436	])
score.addEvent(	["Inharm",	21	,	2.1214,	658.0572,	0.05273436	])
score.addEvent(	["Inharm",	21.75	,	4.7717,	277.2601,	0.08612442	])
score.addEvent(	["Inharm",	21.75	,	4.2415,	311.2103,	0.08612442	])
score.addEvent(	["Inharm",	21.75	,	3.18115,	369.6801,	0.08612442	])
score.addEvent(	["Inharm",	21.75	,	2.12075,	493.8813,	0.08612442	])
score.addEvent(	["Inharm",	21.75	,	3.7113,	522.4561,	0.0645933	])
score.addEvent(	["Inharm",	21.75	,	2.12075,	658.2569,	0.0645933	])
score.addEvent(	["Inharm",	23.5	,	2.25,	246,	0.13913046	])
score.addEvent(	["Inharm",	23.5	,	3,	350,	0.0695652	])
score.addEvent(	["Inharm",	23.5	,	0.75,	528,	0.09275364	])
score.addEvent(	["Inharm",	23.5	,	2,	555.6,	0.09275364	])
score.addEvent(	["Inharm",	23.5	,	1.5,	658,	0.09275364	])
score.addEvent(	["Inharm",	23.5	,	1,	784,	0.13913046	])
score.addEvent(	["Inharm",	31	,	6,	233,	0.1125	])
score.addEvent(	["Inharm",	31	,	4.5,	277,	0.1125	])
score.addEvent(	["Inharm",	31	,	4,	370,	0.1125	])
score.addEvent(	["Inharm",	31	,	2.5,	392,	0.1125	])
score.addEvent(	["Inharm",	31	,	2,	523,	0.075	])
score.addEvent(	["Inharm",	31	,	2,	880,	0.1125	])
score.addEvent(	["Inharm",	31.2	,	5.99145,	146.2089,	0.0703125	])
score.addEvent(	["Inharm",	31.2	,	5.49215,	207.2961,	0.046875	])
score.addEvent(	["Inharm",	31.2	,	3.9943,	277.3963,	0.046875	])
score.addEvent(	["Inharm",	31.2	,	4.99285,	330.1717,	0.03515622	])
score.addEvent(	["Inharm",	31.2	,	2.9957,	466.6667,	0.03515622	])
score.addEvent(	["Inharm",	31.2	,	1.99715,	698.9986,	0.03515622	])
score.addEvent(	["Inharm",	33	,	3.3576,	390.1625,	0.1730769	])
score.addEvent(	["Inharm",	33	,	2.3503,	618.0054,	0.08653848	])
score.addEvent(	["Inharm",	33	,	2.01455,	874.1426,	0.08653848	])
score.addEvent(	["Inharm",	33	,	1.00725,	1167.509,	0.08653848	])
score.addEvent(	["Inharm",	33	,	1.6788,	1387.9061,	0.08653848	])
score.addEvent(	["Inharm",	33	,	1.34305,	1650,	0.08653848	])
score.addEvent(	["Inharm",	36	,	3,	901.2894,	0.0369231	])
score.addEvent(	["Inharm",	36	,	2,	165.5702,	0.0369231	])
score.addEvent(	["Inharm",	36	,	2.75,	461.9943,	0.0369231	])
score.addEvent(	["Inharm",	36	,	2.125,	1479.4499,	0.0369231	])
score.addEvent(	["Inharm",	36	,	0.75,	2181.788,	0.0369231	])
score.addEvent(	["Inharm",	36	,	0.375,	3002.9628,	0.0369231	])
score.addEvent(	["Inharm",	36	,	0.25,	3926.9513,	0.0369231	])
score.addEvent(	["Inharm",	36	,	0.1875,	4940.4011,	0.0369231	])
score.addEvent(	["Inharm",	36	,	0.1,	6013.937,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	3,	636.3181,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	2,	116.894,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	2.75,	326.1719,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	2.125,	1044.5043,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	0.75,	1540.361,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	0.375,	2120.1175,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	0.25,	2772.4613,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	0.1875,	3487.9656,	0.0369231	])
score.addEvent(	["Inharm",	36.075	,	0.1,	4245.8911,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	3,	400.3582,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	2,	73.5473,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	2.75,	205.2206,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	2.125,	657.1805,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	0.75,	969.1633,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	0.375,	1333.9341,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	0.25,	1744.3754,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	0.1875,	2194.5559,	0.0369231	])
score.addEvent(	["Inharm",	36.15	,	0.1,	2671.4269,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	4,	535.745,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	2.66665,	98.4183,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	3.66665,	274.6189,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	2.83335,	879.4155,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	1,	1296.8997,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	0.5,	1785.0229,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	0.33335,	2334.2607,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	0.25,	2936.6762,	0.0369231	])
score.addEvent(	["Inharm",	36.2	,	0.13335,	3574.808,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	5,	284.3123,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	3.33335,	52.2292,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	4.58335,	145.7364,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	3.54165,	466.6934,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	1.25,	688.2464,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	0.625,	947.2865,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	0.41665,	1238.7593,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	0.3125,	1558.4527,	0.0369231	])
score.addEvent(	["Inharm",	36.25	,	0.16665,	1897.1003,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	3,	1350,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	2,	248,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	2.75,	692,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	2.125,	2216,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	0.75,	3268,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	0.375,	4498,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	0.25,	5882,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	0.1875,	7400,	0.0369231	])
score.addEvent(	["Inharm",	36.275	,	0.1,	9008,	0.0369231	])
score.addEvent(	["Inharm",	37.5	,	3.2378,	691.823,	0.02571426	])
score.addEvent(	["Inharm",	37.5	,	2.91405,	694.9115,	0.01714284	])
score.addEvent(	["Inharm",	37.5	,	2.1046,	1136.5664,	0.02571426	])
score.addEvent(	["Inharm",	37.5	,	1.7808,	1141.8168,	0.04628574	])
score.addEvent(	["Inharm",	37.5	,	1.0523,	1470.1239,	0.06857142	])
score.addEvent(	["Inharm",	37.5	,	1.13325,	2100.177,	0.04285716	])
score.addEvent(	["Inharm",	37.5	,	0.80945,	2470.7965,	0.03771426	])
score.addEvent(	["Inharm",	37.5	,	0.64755,	3378.8142,	0.03428574	])
score.addEvent(	["Inharm",	37.5	,	0.48565,	3706.1947,	0.03428574	])
score.addEvent(	["Inharm",	37.5	,	0.3238,	4645.0973,	0.02571426	])
score.addEvent(	["Inharm",	37.5	,	0.24285,	5028.0708,	0.03428574	])
score.addEvent(	["Inharm",	38.3	,	9.97855,	464.9978,	0.1125	])
score.addEvent(	["Inharm",	38.3	,	7.98285,	464.1961,	0.0675	])
score.addEvent(	["Inharm",	38.3	,	7.4839,	606.3011,	0.0675	])
score.addEvent(	["Inharm",	38.3	,	5.4882,	608.3054,	0.0225	])
score.addEvent(	["Inharm",	38.3	,	4.98925,	776.6667,	0.045	])
score.addEvent(	["Inharm",	38.3	,	3.4925,	935.0065,	0.09	])
score.addEvent(	["Inharm",	38.3	,	2.49465,	945.028,	0.045	])
score.addEvent(	["Inharm",	38.3	,	1.9957,	1082.3226,	0.045	])
score.addEvent(	["Inharm",	38.3	,	1.4968,	1242.6667,	0.0225	])
score.addEvent(	["Inharm",	38.3	,	1.2473,	1563.3548,	0.03375	])
score.addEvent(	["Inharm",	38.3	,	1.4968,	1723.6989,	0.045	])


score.play()

s.gui(locals())
