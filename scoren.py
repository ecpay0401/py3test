score = int(input('輸入分數：'))
if score >= 90:
    print('得 A')
else:
    if 90 > score >= 80:
        print('得 B')
    else:
        if 80 > score >= 70:
            print('得 C')
        else:
            if 70 > score >= 60:
                print('得 D')
            else:
                print('不及格')