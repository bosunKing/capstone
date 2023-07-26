from mylib.getchar import Getchar  #위에 라이브러리랑 함수를 같이 적어놓음으로 밑에서 getchar.000할것을 간소화함 . 고로 밑에서 getchar() 사용가능


def main(args=None):
    kb = Getchar()
    key = ''
    
    while key!='Q':
    
        key = kb.getch()
        if key != '':
            print(key)
        else:
            pass
        

if __name__ == '__main__': # python전역변수 모듈의 이름이 main과 같으면~~ 이라는 의미 저 위에 main을 호출해서 사용해라 .
    main()

