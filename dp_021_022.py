#!/usr/bin/env python3

import numpy as np
from time import time
from copy import copy

time_start = time()

# Function : 対象のファイル名一覧を返す（一覧が記載されている、file_list.txt）
#            行(0~3)：0 = city011, 1 = city012, 2 = city021, 3 = city022
#            列(0~99)：0 = _001, 1 = _002, ..... , 98 = _099, 99 = _100
def TargetFile():
    f_l = []
    f_fl = []

    with open("file_list.txt", "r") as f:
        file = f.read().split("\n")

        for a in range(0, 400):

            if (a > 0) and (0 == a % 100):
                f_fl.append(copy(f_l))
                f_l = []

            f_l.append(copy(file[a]))

        f_fl.append(copy(f_l))

    arr_f_fl = np.array(f_fl)
    #print(arr_f_fl)

    return arr_f_fl

# Function : fileを読み込む
def ReadFile(FileName):
    # 純粋なリストで読み込み
    ft = []  # 行を記録。一行読み終わったら、fu[]に行ごと代入して、初期化される
    fu = []  # 行列を記録。ft[]をそのまま行(１つの要素)として得る。

    with open(FileName, 'r') as f:  # 別ファイルを読み込む際の、変更箇所

        file = f.read()  # 変数にテキストを読ませる。type:String
        #print(file)
        count = 0  # for文内カウンタ用。未使用

        for i in (file.split(" ")):  # " "ごとに文字列を区切り、１要素ずつ読む

            if i[:1] == 'c':  # 初めの3行に対する処理。3行を読み飛ばして、[0][0]の値のみ行列に入れる
                #print(i)
                val00 = ""
                indent = 0

                for b in range(0, len(i)):  # 3つ目の"\n"までを無視。以降が要素[0][0]の値となる。
                    if i[b] == "\n":
                        indent += 1
                    if indent == 3:
                        val00 += i[b]

                ft.append(copy(float(val00)))
                count += 1
                continue

            if i[:1] == '\n':  # 行の初めの値は、"\n"に連続している。為、"\n"を読み飛ばしてappendする必要がある

                if i == '\n':  # テキスト最後の改行かの判断
                    fu.append(copy(ft))  # 行列の最後の行をappend
                    continue  # continueしているが、そのままループを抜けることになる

                fu.append(copy(ft))  # 行列の行をappend
                ft = []  # 行の記録を初期化
                ft.append(copy(float(i[1:])))  # 行の最初の値を、"\n"を読み飛ばして、append
                count += 1
                continue

            ft.append(copy(float(i)))  # 行の値を、append
            count += 1

        arr_fu = np.array(fu)  # 行列を、numpy.array型に変換(計算のしやすさ、見た目の良さの為)

        # 結果の出力(行列、行列のサイズ)
        #print("ARRAY : " + FileName)
        #print(arr_fu)
        #print("SHAPE : " + FileName)
        #print(arr_fu.shape)

        return arr_fu


if __name__ ==  '__main__':
    # 行(0~3) ：0 = city011, 1 = city012, 2 = city021, 3 = city022
    # 列(0~99)：0 = _001, 1 = _002, ..... , 98 = _099, 99 = _100
    targetfile = TargetFile()  # 対象となるファイル名の一覧を、行列([0~3][0~99])で返される。

# 以下、４つのデータセット全ての、１００単語全ての情報を、４つのデータセットそれぞれの配列に適用（関数に参照渡しでやらせるのがスマートかも）

    # 話者０１、１回目発声
    Speaker_01_1 = []
    sp011_shape = []
    for a in range(0, 100):
        array_data = ReadFile(FileName=targetfile[0][a])
        Speaker_01_1.append(copy(array_data))
        array_data = []  # 恐らく、初期化に意味はない。気休め

        sp011_shape.append(copy(Speaker_01_1[a].shape))  # type : tuple
        #print("SHAPE:" + targetfile[0][a])
        #print(Speaker_01_1[a].shape)

    # 話者０１，２回目発声
    Speaker_01_2 = []
    sp012_shape = []
    for a in range(0, 100):
        array_data = ReadFile(FileName=targetfile[1][a])
        Speaker_01_2.append(copy(array_data))
        array_data = []

        sp012_shape.append(copy(Speaker_01_2[a].shape))
        #print("SHAPE:" + targetfile[1][a])
        #print(Speaker_01_2[a].shape)

    # 話者０２，１回目発声
    Speaker_02_1 = []
    sp021_shape = []
    for a in range(0, 100):
        array_data = ReadFile(FileName=targetfile[2][a])
        Speaker_02_1.append(copy(array_data))
        array_data = []

        sp021_shape.append(copy(Speaker_02_1[a].shape))
        #print("SHAPE:" + targetfile[2][a])
        #print(Speaker_02_1[a].shape)

    # 話者０２、２回目発声
    Speaker_02_2 = []
    sp022_shape = []
    for a in range(0, 100):
        array_data = ReadFile(FileName=targetfile[3][a])
        Speaker_02_2.append(copy(array_data))
        array_data = []

        sp022_shape.append(copy(Speaker_02_2[a].shape))
        #print("SHAPE:" + targetfile[3][a])
        #print(Speaker_02_2[a].shape)

    # 各データセット、確認出力
    #print(len(Speaker_01_1))
    #print(len(Speaker_01_2))
    #print(len(Speaker_02_1))
    #print(len(Speaker_02_2))
    #print(sp011_shape)
    #print(sp012_shape)
    #rint(sp021_shape)
    #print(sp022_shape)
    #print(len(sp011_shape))
    #print(len(sp012_shape))
    #print(len(sp021_shape))
    #print(len(sp022_shape))

    #print(sp011_shape[0][0])

# 以下、局所距離の計算

    dis_part = 0
    dis_part_squ = 0
    LD_cell = 0
    LD_line = []
    LocalDistance = []
    DataSetLocalDistance_011_012 = []
    # DataSetLocalDistance_011_012_all = []  # 未知１-テンプレ１００を１セットとして、１００セット文の配列（縦）にする案。
                                            # DataSetLocalDistance_011_012を、100*100の縦配列にしても良い。
    
    # 全単語で、総当りを行うための改良、必要
    # 局所距離の行列の生成

    """ 100_time:1000s , 1_ime:9s """
    # for a in range(0, 100):  # データセット内、全単語数  これだと、同一単語同士の比較のみになってしまう
    for a in range(0, 100):  # a = 未知単語の数

        # これをsp012_shape[x][0]とすれば、全単語同士の総当りになる
        for x in range(0, 100):  # x = テンプレ単語の数

            # 以下、未知単語１とテンプレ単語１００とのマッチング、局所距離の全取得
            for b in range(0, sp021_shape[x][0]):  # テンプレート、フレーム数Iに相当 (ex.city011_001 : 61)

                for c in range(0, sp022_shape[a][0]):  # 未知、フレーム数Jに相当 (ex.city012_001 : 64)

                    for d in range(0, 15):  # 次元数１５
                        dis_part = Speaker_02_1[x][b][d] - Speaker_02_2[a][c][d]  # 話者どうしの引き算
                        dis_part_squ = dis_part * dis_part  # ２乗
                        LD_cell += dis_part_squ  # d(i, j)^2 に相当
                        dis_part = 0  # 気休めの初期化
                        dis_part_squ = 0  # 気休めの初期化
                        #print("＿＿＿＿" + str(d))
 
                    LD_line.append(copy(np.sqrt(LD_cell)))  # d(i, j)で配列を作成（要素：c = j） (ex.64)
                    #print(len(LD_line))
                    LD_cell = 0
                    #print("＿＿＿" + str(c))
                
                LocalDistance.append(copy(LD_line))  # d(i, j)で行列を作成（要素：行＝b = i、列＝c = j）(ex.(64,61))
                #print((np.array(LocalDistance)).shape)
                LD_line = []
                #print("＿＿" + str(b))
                
            DataSetLocalDistance_011_012.append(copy(LocalDistance))  # 行列LocalDistanceの配列 (要素数：未知単語の数に依存する)
            #print((np.array(DataSetLocalDistance_011_012)).shape)
            LocalDistance = []
            #print("＿" + str(a))

    #NumpyDSLD = np.array(DataSetLocalDistance_011_012)
    #print(NumpyDSLD[0])
    #print(NumpyDSLD)
    #print(NumpyDSLD.shape)
    #print(len(NumpyDSLD))
    #print(len(NumpyDSLD[0]))
    #print(len(NumpyDSLD[0][0]))
    #print(DataSetLocalDistance_011_012[0][0][0])
    #print(DataSetLocalDistance_011_012[0][60][63])  # 行列の要素を探索（[行=縦][列=横]）

    time_end_1 = time()
    print(time_end_1 - time_start)

# 以下、累積距離の計算
    
    DP_0 = 0
    DP_1 = 0
    DP_2 = 0
    DP_3 = 0
    DP_line = []
    DP_array = []
    DP_array_all = []  # 未知１、テンプレ１００。各累積距離の雛形。初期条件、境界条件を定義。後に、累積距離を記録

    for x in range(0, 100):  # Unkonwn

        for y in range(0, 100):  # Template
            xy = (x*100)+y

            j = 0
    # 以下、初期条件の設定
            DP_0 = DataSetLocalDistance_011_012[xy][0][0]
            DP_line.append(copy(DP_0))
            j += 1

    # 以下、境界条件の設定
            for a in range(1, sp022_shape[x][0]):  # 列（未知）の境界条件
                DP_1 = DP_line[j-1] + DataSetLocalDistance_011_012[xy][0][a]
                DP_line.append(copy(DP_1))
                j += 1

            DP_array.append(copy(DP_line))
            DP_line = [0]*j
            #print(DP_line)

            i = 1
            for a in range(1, sp021_shape[y][0]):  # 行（テンプレート）の境界条件
                DP_2 = DP_array[i-1][0] + DataSetLocalDistance_011_012[xy][a][0]
                #print(DP_array[i-1][0])
                #print(DataSetLocalDistance_011_012[xy][a][0])
                #print(DP_2)
                DP_line[0] = copy(DP_2)
                #print(DP_line)
                #print(DP_line)
                DP_array.append(copy(DP_line))
                #print(DP_array)
                i += 1
                DP_2 = 0
                DP_line [0]*j

            DP_array_all.append(copy(DP_array))
            #np1 = np.array(DP_array)
            #print(DP_array)
            #print(np1)
            #npDP_array_all = np.array(DP_array_all)
            #print(npDP_array_all[0])
            #print(y)
            #print(DP_array_all[y])
            #print(len(DP_array_all))

            DP_0 = 0
            DP_1 = 0
            DP_2 = 0
            i = 0
            j = 0
            DP_line = []
            DP_array = []

    time_end_3 = time()
    print(time_end_3 - time_start)
    
    #print(len(DP_array_all))

    # 以下、各累積距離計算

    weight = np.sqrt(3)
    vertical = 0  # 縦の累積距離
    width = 0  # 横の累積距離
    diagonal = 0  # 斜めの累積距離
    T = 0
    minT = 0
    check_list = []  # 0 = fail, 1 = success
    Mdistance = 0
    Mdistance_list = []
    Mdistance_list_min = []
    DP_line_T = []
    DP_array_all_T = []

    for x in range(0, 100):  # Unknown

        for y in range(0, 100):  # Template
            xy_2 = (x*100)+y
            for i in range(1, sp021_shape[y][0]):

                for j in range(1, sp022_shape[x][0]):
                    width = DP_array_all[xy_2][i][j-1] + DataSetLocalDistance_011_012[xy_2][i][j]  # 横の累積距離
                    vertical = DP_array_all[xy_2][i-1][j] + DataSetLocalDistance_011_012[xy_2][i][j]  # 縦の累積距離
                    diagonal = DP_array_all[xy_2][i-1][j-1] + (weight * DataSetLocalDistance_011_012[xy_2][i][j])  # 斜めの累積距離（重み：２倍）
                    DP_array_all[xy_2][i][j] = copy(min(width, vertical, diagonal))
                    Mdistance += copy(min(width, vertical, diagonal))

                    width = 0
                    vertical = 0
                    diagonal = 0
            
            T = DP_array_all[xy_2][sp021_shape[y][0]-1][sp022_shape[x][0]-1] / (sp021_shape[y][0] + sp022_shape[x][0])
            DP_line_T.append(copy(T))
            Mdistance_list.append(copy(Mdistance))

            Mdistance = 0
            T = 0
        
        minT = copy(DP_line_T.index(min(copy(DP_line_T))))
        Mdistance_list_min.append(min(copy(Mdistance_list)))
        if x == minT:
            check_list.append(1)
        else:
            check_list.append(0)
        #print(" Unknown :" + str(x) + "/ Template :" + str(minT))
        DP_line_T = []
        minT = 0
    
    print(check_list)
    print("021_022, 最小累積距離[最大値：最小値：平均]：[" + str(max(copy(Mdistance_list_min))) + "：" + str(min(copy(Mdistance_list_min))) + "：" + str(copy(sum(Mdistance_list_min)/len(Mdistance_list_min))) + "]")
    print("021_022, 一致率：" + str(check_list.count(1)) + " %")

    time_end_2 = time()
    print(time_end_2 - time_start)
