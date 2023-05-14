class Game :
    def __init__(self):
        print ('welcome In Full game .....^ _ ^')
        print ('choose your game from our collection ')
        print ('press[1] : play even_odd game ')
        print ('press[2] : play sum average game ')
        print ('press[3] : play multiplication table game')

        self.choices()

    def choices(self):
        while True:
            user_choice = input('enter your choice : ')

            try :
               user_choice = int(user_choice)
               if user_choice == 1 :
                  self.Even_Odd_Game() 
                
               elif user_choice == 2 :
                    self.Sum_Avarage_Game()

               elif user_choice == 3 :
                    self.Multiplication_Game()
               else:
                   print('please choose between 1,2 or 3')
            except ValueError:
               print ('please enter a vaild number')


    def Even_Odd_Game (self):
        print('welcome in the even-odd game')
        print('please enter a number ... And i will tell you if it even or odd')
        print ( 'if you want close the game enter x ')

        while True:
            number=input('enter a number:')
            if number == 'x' :
                print ( 'closing the game ')
                print ( 'thanks ...')
                break

            try :
                number=int(number)
                if number % 2 == 0 :
                    print('even number')
                else:
                    print ('odd number')
            except ValueError:
                print ('please enter a valid number ')
            print ( '----------------------------------')


    def Sum_Avarage_Game(self):
        print('this game will take several numbers amd print the avarage of them')
        count=int(input('how many numbers would you like to sum :'))
        current_count = 0
        summ = 0

        while current_count < count :
            number = float(input('enter the number :'))
            summ += number
            current_count += 1
        print ('sum of all numbers = ' , summ)
        print ( 'avarage of all numbers=' , summ/count)


    def Multiplication_Game(self):
        print ('welcome in multiplication app')
        print ('please enter the first number and the last number of the multiplication table')


        start=int(input('enter the first number of the table :'))
        end =int(input('enter the last number of the table :'))
        for x in range ( start , end+1):
            for y in range (1,13):
                print ( x ,'x' , y ,'=' ,x*y)
            print ( '--------------------')

game1 = Game()
