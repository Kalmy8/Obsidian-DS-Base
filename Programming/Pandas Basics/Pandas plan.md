1) загружать и смотреть общую инфу
2) выбирать колонки/строчки и сортировать
3) научились melt и groupby (трансформировать) датасет
4) научиться датасеты друг с другом дружить (соединять/делать join) 
5) научиться выполнять агрегации (считать средние/нормализовать данные)
6) научиться менять данные сами (создавать колонки, изменять значения, apply, map)

--- Дальше идет праткическое применение ---
7) работать с выбросами и находить их и ненормальными значениями
8) строить красивые графики:
Идейно 2д график показывает:
- либо зависимость двух величин:
    - величины могут быть дискретные или непрерывные
    
    - 2 непрерывные дают lineplot/scatterplot
    
    - 2 дискретные дают матрицу сопряженности (crosstab/heatmap)
    
    - дискретная + непрерывная дает barplot    

- либо характеристику одной величины:
    - гистограмма/kdeplot дает частоту встречаемости величины
    - piechart дает доли 


9) Прочитать короткий курс статистики: про проверку гипотез и прочее (здесь уже реальные датасеты)



статистика в конце:
графики
crosstab для матриц сопряженности
corr Для корреляций
хитмапы
и тому подобное

нужны реальные пример датасетов, научиться ставить и проверять гипотезы!

todo не забыть Injection memmory usage после categories


доделать и использовать (идейно понравилась задача но пока некуда ее):

4. Text Data Processing:
```python
# Product reviews data
import pandas as pd

data = {
    'product_id': ['A001', 'A001', 'A002', 'A002', 'A003', 'A003', 'A004', 'A004'],
    'rating': [4, 5, 2, 1, 5, 4, 3, 4],
    'review_text': [
        "This product is great and works as expected.",
        "Love this! Best purchase I've made in 2023.",
        "Disappointed with the quality, broke after 2 weeks of use.",
        "Terrible product, doesn't work at all. Waste of money.",
        "Excellent product, highly recommend for all users.",
        "Very good performance and easy to use interface.",
        "Average product, nothing special but gets the job done.",
        "Good value for money, happy with my purchase."
    ]
}
reviews = pd.DataFrame(data)
```
Tasks:
- Extract word counts from each review
- Identify common positive and negative words
- Categorize reviews as positive (4-5), neutral (3), or negative (1-2)
- Create a function to check if reviews contain specific keywords
- Calculate the average rating when specific words appear in reviews
- Visualize the relationship between review length and rating

