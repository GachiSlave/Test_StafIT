# Примеры запуска скрипта:
![economic1](https://github.com/GachiSlave/Test_StafIT/blob/ff184a6be94cbef26e336f4af1ec7ecd415de28e/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20economic1.png)
![economic2](https://github.com/GachiSlave/Test_StafIT/blob/ff184a6be94cbef26e336f4af1ec7ecd415de28e/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20economic2.png)
![economic1+2](https://github.com/GachiSlave/Test_StafIT/blob/ff184a6be94cbef26e336f4af1ec7ecd415de28e/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20economic1%2Beconomic2.png)
![Свободный запрос](https://github.com/GachiSlave/Test_StafIT/blob/ff184a6be94cbef26e336f4af1ec7ecd415de28e/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8.png)

# Добавления новых видов отчётов
В скрипте уже можно получать среднии для разных числовых столбцов как например gdp, unemployment и других числовых стобцов передавая имя столбца после тире:
```
python .\main.py --files economic1.csv economic2.csv --report average-unemployment
```
```
python .\main.py --files economic1.csv economic2.csv --report average-gdp
```
Я старался реализовать что то похожее на работу pandas
В процессе получения яотчёта о среднем ВВП по странам я написал промежуточные функции которые можно будет использовать для создания новых отчётов как:
read_csv - считывает csv файл в виде словаря где ключи это столбцы: {col1: [], col2: [], ... , coln: []}
group_by - группирует данные по уникальным категориям, дальше к этому предтавлению можно принимать агрегирующие функции average, max, min  и тд для расширения отчётов 
average - агрегирующая функция средних
sort_by - сортирует данные
average_report - pipeline где поочередне применяются промежуточные функции для получения отчёта, можно будет добавить новые виды pipelin'ов для новых отчётов
или реализовать автоматическую сборку pipelin'a на основе данных их --report

