На собеседованиях нас часто просят описать от и до, как мы стали бы решать некоторую ML задачу, не вдаваясь в детали имплементации

##### [Бабушкин 1: Задача ранжирования рекламы](https://www.youtube.com/watch?v=VPg2Uu1MYgI&list=PLBRXq5LaddfzDBjg6soIwJJA2klXXs6ni&index=19&ab_channel=karpov.courses)
- Сначала описываем данные, как мы планируем их собирать, сколько, какие фичи включить в модель...
	- Хорошо, если кандидат строит предположения сам, а не просто спрашивает о наличных данных
	- Хорошо, если мы учтем баланс/дисбаланс данных
	- Как бить train/test?
- Описываем метрики, которые будем оптимизировать, лучше накидать несколько вариантов, их плюсы и минусы.  
- Описываем саму модель, подход к решению задачи с учетом данных и метрик. Описываем лосс
- Описывеам, как будем проводить эксперименты с моделью? A/B тесты? Что, если параллельно разрабатывается несколько моделей? Как будешь "дружить" свою модель с остальными?
	- Если моделей и вариаций их много (тысячи), то мы часто будем получать ошибку 1го рода (ложноположительный результат). Это к поправке Бонферонни и т.п.
- Рекомендательные системы: обсудить проблему **feedback-loop:**  если я учу модель рекомендовать рекламу, то она в какой-то момент начинает обучаться рекомендовать то, что она уже рекомендовала (в train-data нарастает дисбаланс)
	- Хорошо обсудить парные лоссы

Хорошо пользоваться доской/рисовать схемы по ходу собеса, чтобы не забыть ни один из вопросов

##### [ML System Design с Валерием Бабушкиным | Выпуск 2 | Собеседование | karpov.courses - YouTube](https://www.youtube.com/watch?v=WKYPQtqE-m0&list=PLBRXq5LaddfzDBjg6soIwJJA2klXXs6ni&index=17)

Дано: Маркетплейс типа ВБ/Яндекс. Есть карточка товара. Какую цену следует ему поставить для максимизации оборота, если нам нельзя продавать себе в минус?

Решение:
Фичами становятся признаки товара, пользователя, и цена, а таргетом - вероятность покупки. Получив для каждого пользователя вероятность покупки с каждой ценой, можем вывести матожидание прибыли

Сделав groupby по цене (bins), можем найти наивысшее матожидание

Были затронуты проблемы feedback loop и A/B тестов, того, как вообще сравнивать готовые модели по эффективности

**Особенно важно придерживаться общей структуры:**
- Данные (как добывать, какие добывать, зачем)
- Фичи и таргет
- Лосс, подходящий к задаче
- Метрики, подходящие к задаче
- A/B тестирование, выбор наилучшей модели
- Проблема feedback loop
- Проблемы, связанные с течением времени


##### [ML System Design с Валерием Бабушкиным | Выпуск 3 | Собеседование | karpov.courses - YouTube](https://www.youtube.com/watch?v=3X-TAuWdIAc)

Задача матчинга: Есть маркетплейс, он позволяет разным продавцам размещать свои товары. Представим, что у нас продается 15й айфон модели Pro Max. Необходимо для этой модели найти все офферы, которые продавцы выложили на нашу площадку (в карточках товаров могут быть неточности. атрибуты могут быть заполнены криво. полагаться можно на title + на фото товара) 

- Когда обсуждаем данные, обсуждаем сразу и X и Y