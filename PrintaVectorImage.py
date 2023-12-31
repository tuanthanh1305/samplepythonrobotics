#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()

#endregion VEXcode Generated Robot Configuration
dot = [[2,89],
[4,85],
[6,82],
[8,78],
[11,75],
[13,71],
[15,68],
[18,64],
[20,60],
[22,57],
[22,53],
[19,50],
[17,46],
[15,42],
[13,39],
[12,35],
[15,37],
[18,40],
[20,44],
[23,47],
[25,51],
[27,55],
[25,58],
[23,62],
[21,66],
[19,69],
[17,73],
[14,76],
[12,80],
[10,83],
[7,87],
[5,90],
[1,93],
[14,86],
[17,82],
[20,79],
[21,82],
[19,86],
[16,90],
[13,93],
[12,90],
[30,83],
[28,80],
[26,76],
[25,72],
[26,68],
[28,64],
[30,61],
[32,57],
[35,53],
[37,50],
[39,46],
[42,43],
[44,40],
[47,36],
[50,36],
[48,40],
[46,43],
[44,47],
[41,50],
[39,54],
[37,57],
[35,61],
[32,65],
[30,68],
[28,72],
[30,75],
[32,79],
[34,83],
[37,86],
[39,90],
[38,93],
[35,90],
[32,87],
[40,82],
[38,79],
[36,75],
[35,71],
[36,70],
[39,73],
[41,77],
[43,80],
[45,84],
[48,87],
[49,91],
[47,92],
[45,89],
[42,86],
[58,68],
[58,64],
[58,60],
[58,56],
[58,51],
[58,47],
[59,43],
[62,39],
[65,37],
[69,35],
[73,34],
[77,34],
[81,35],
[85,37],
[89,40],
[91,43],
[92,47],
[93,51],
[93,56],
[92,60],
[91,64],
[89,68],
[86,71],
[82,73],
[78,73],
[74,73],
[70,73],
[66,72],
[65,75],
[65,79],
[65,84],
[65,88],
[64,92],
[60,92],
[58,89],
[58,84],
[58,80],
[58,76],
[58,71],
[83,63],
[84,59],
[84,55],
[84,50],
[83,46],
[82,43],
[78,43],
[74,42],
[69,43],
[67,46],
[66,50],
[65,54],
[66,58],
[67,62],
[70,65],
[74,66],
[78,66],
[141,86],
[140,82],
[142,79],
[146,80],
[148,84],
[145,87],
[107,72],
[103,70],
[101,66],
[100,62],
[100,58],
[100,54],
[100,49],
[100,45],
[100,41],
[100,37],
[104,35],
[106,38],
[107,42],
[107,46],
[107,51],
[107,55],
[107,59],
[108,63],
[112,66],
[116,66],
[120,66],
[123,63],
[124,59],
[124,54],
[124,50],
[124,46],
[124,42],
[125,37],
[128,35],
[131,37],
[131,41],
[131,46],
[131,50],
[131,54],
[131,59],
[131,63],
[130,67],
[127,70],
[123,72],
[119,73],
[115,73],
[111,73],
[141,72],
[141,68],
[140,64],
[140,60],
[140,56],
[140,51],
[140,47],
[140,43],
[140,39],
[142,35],
[146,36],
[148,40],
[148,44],
[148,48],
[148,53],
[148,57],
[148,61],
[148,65],
[147,70],
[145,73],
[161,70],
[158,67],
[157,63],
[157,59],
[157,55],
[157,50],
[157,46],
[157,42],
[157,38],
[161,36],
[163,39],
[164,43],
[164,47],
[164,51],
[164,56],
[165,60],
[166,64],
[169,66],
[174,66],
[177,64],
[178,60],
[179,56],
[179,52],
[179,47],
[179,43],
[180,39],
[182,36],
[186,37],
[186,42],
[187,46],
[187,50],
[187,54],
[187,58],
[188,63],
[191,66],
[195,66],
[199,65],
[201,61],
[201,57],
[202,53],
[202,49],
[202,45],
[202,40],
[204,36],
[207,35],
[210,38],
[210,42],
[210,47],
[210,51],
[210,55],
[210,59],
[209,64],
[207,67],
[204,70],
[201,72],
[197,73],
[192,74],
[188,73],
[185,71],
[181,71],
[177,73],
[173,73],
[169,73],
[164,72],
[8,49],
[6,45],
[4,42],
[2,38],
[2,35],
[5,38],
[8,41],
[10,44],
[13,48],
[15,51],
[17,55],
[16,58],
[13,55],
[11,52],
[29,48],
[30,44],
[33,40],
[35,37],
[39,35],
[38,39],
[36,43],
[33,47],
[4,17],
[3,12],
[3,8],
[4,9],
[5,13],
[5,18],
[4,22],
[4,21],
[46,20],
[43,19],
[39,18],
[37,14],
[37,9],
[37,7],
[38,11],
[40,15],
[43,16],
[45,12],
[47,9],
[47,13],
[47,17],
[47,22],
[66,22],
[70,20],
[69,16],
[66,14],
[63,11],
[65,7],
[69,6],
[73,7],
[69,7],
[66,9],
[67,13],
[71,16],
[73,19],
[70,22],
[66,23],
[126,17],
[126,13],
[125,9],
[125,6],
[127,9],
[127,13],
[127,18],
[127,21],
[169,19],
[169,15],
[170,11],
[171,10],
[171,14],
[171,18],
[171,22],
[200,21],
[202,17],
[203,13],
[204,9],
[204,11],
[205,15],
[205,19],
[208,22],
[205,23],
[201,23],
[11,18],
[9,15],
[9,10],
[11,7],
[15,6],
[18,8],
[19,12],
[18,16],
[15,19],
[17,12],
[15,8],
[12,8],
[11,12],
[12,16],
[15,16],
[25,18],
[23,15],
[23,10],
[25,7],
[29,6],
[32,8],
[33,12],
[32,16],
[29,19],
[25,18],
[30,8],
[26,8],
[25,12],
[26,16],
[29,16],
[55,18],
[57,14],
[57,10],
[55,7],
[55,6],
[58,8],
[59,12],
[58,16],
[55,18],
[97,15],
[98,12],
[101,11],
[98,14],
[101,17],
[102,19],
[98,19],
[112,17],
[110,14],
[111,9],
[114,6],
[118,6],
[121,8],
[118,9],
[114,8],
[112,11],
[113,15],
[116,17],
[119,15],
[120,17],
[116,19],
[133,17],
[132,13],
[132,9],
[135,6],
[139,6],
[141,9],
[142,13],
[140,17],
[137,19],
[139,12],
[138,8],
[134,8],
[133,12],
[134,16],
[138,16],
[147,16],
[146,12],
[146,9],
[148,13],
[150,17],
[153,16],
[155,12],
[155,8],
[155,9],
[155,13],
[154,17],
[150,19],
[162,18],
[161,14],
[161,9],
[162,10],
[163,14],
[166,18],
[177,17],
[180,14],
[179,10],
[176,7],
[178,6],
[182,8],
[182,13],
[180,17],
[177,19],
[188,17],
[186,14],
[189,13],
[190,17],
[194,15],
[194,11],
[191,7],
[188,5],
[192,6],
[195,9],
[196,13],
[195,17],
[191,19],
[91,15],
[90,11],
[88,8],
[86,11],
[84,11],
[85,7],
[87,3],
[90,0],
[89,3],
[90,7],
[92,11],
[92,16],
[105,15],
[105,10],
[101,7],
[97,5],
[100,1],
[105,0],
[107,4],
[107,9],
[106,14],
[105,17],
[103,2],
[99,2],
[101,5]]
for i in range(500):
    brain.screen.draw_pixel(dot[i][0], dot[i][1])


