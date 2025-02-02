---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Excalidraw Data
## Text Elements
Ядерная оценка плотности вероятности
(KDE) ^6nyzzPBn

Обыкновенно, для оценки плотности вероятности распределения некоторой величины X 
строят гистограмму, примерно по следующему алгоритму:

    1) Выбираем самое наименьшее и наибольшее значения Х
    2) Разбиваем расстояние между ними на равные интервалы
    3) Для каждого интервала высоту столбца определяем равным количеству 
       наблюдений, попавших в него.

Данный подход несет в себе 2 ключевые проблемы:
    1) Особенности истинного распределения скрадываются, потому как в интервал
      некоторой ширины попадают как большие, так и меньшие значения Х. Чем больше 
      ширина, тем сильнее выражен этот эффект:











    2) Полученная функция в любом случае будет кусочно-заданной, а не гладкой

Для решения обеих проблем решено внести в алгоритм 2 ключевых изменения:
    1) Вместо "прямоугольничков" для изображения наблюдений использовать некоторую
    гладкую симметричную неотрицательную функцию (называемую ядром). Данными
    свойствами обладает в принципе любая из стандартных плотностей вероятностей

    2) Вместо разбиения участка на равные интервалы позволим каждому наблюдению
    вносить вклад в распределении именно в том месте, где он расположен

Математически доказывается, что при таком подходе приближение действительно 
сходится к искомой плотности вероятности

     ^0Bulx8pe

## Embedded Files
62927a6596fa1991cdd94dfda6d566ac45cc2e98: [Pasted Image 20231228011310\_713.png](📁%20files/Pasted%20Image%2020231228011310_713.png)
bfef03817b1d622c9f33176a040fdb6b4bd8dff6: [Pasted Image 20231228011341\_759.png](📁%20files/Pasted%20Image%2020231228011341_759.png)

%%
## Drawing
```compressed-json
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
```
%%