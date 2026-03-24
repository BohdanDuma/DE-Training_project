#!/bin/bash
#variable for test ekstactor
TEST='python test.py'
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
                ;;
            3)
                echo "Запуск повного циклу тестів..."
                ;;
            q) 
                echo "BYE-BYE"
                exit 0
                ;;
            *)
                echo "Bad command. Try one more time from list"
        esac
    done