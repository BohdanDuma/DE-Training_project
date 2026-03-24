#!/bin/bash
#variable for test ekstactor
TEST='python test.py'
LOG='Logs.txt'
#test menu logik
MENU() {
    echo -e "\n--- DataAnalyzer Testing Menu ---"
    echo "1 - Extraction Test (JSON Matrix)"
    echo "2 - Benchmark (Manual vs NumPy)"
    echo "3 - Run All Tests & Save to Log"
    echo "q - Quit"
}
while true
    do
        MENU
        read OPTION
        case $OPTION in
            1)
                echo "Введіть матрицю (напр. '[[1,2],[3,4]]'):"
                read MATRIX
                $TEST "$MATRIX"
                ;;
            2)

                echo "Введіть числа через пробіл:"
                read -a ARR
                $TEST "$ARR"
                ;;
            3)
                echo "Запуск повного циклу тестів..."
                echo -r "---TEST ($date)($time)---"
                $TEST '[[10,20],[30,40]]' >> log.txt && echo "Extraction done"
                $TEST 1 2 3 4 5 >> log.txt $$ echo "Speed test done"
                echo "results in $LOG"
                ;;
            q) 
                echo "BYE-BYE"
                exit 0
                ;;
            *)
                echo "Bad command. Try one more time from list"
        esac
    done