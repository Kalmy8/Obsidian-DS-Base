While building a tree, we are relying on some **scoring function** $\large S$ which will show as how good is tree in splitting the training data. 

This function can be stated as:
$$|R|\cdot S(R) - |R_{right}|\cdot S(R_{right})-|R_{left}|\cdot S(R_{left}) \to max,$$
- where $S(R)$ - function $S$ output in root node $R$;
- $S(R_{left}),S(R_{right})$ — outputs in left and right child nodes after split;
-   $∣X∣$ — number of elements in the node $X$.

Alternatively, you can use some other popular functions like:
$$(MSE)\ L_2(g,p) = \sum_{i=1}^N (p_i - g_{i)^2},$$

$$(Cosine\ similarity)\ Cosine(g,p) = \frac{\sum_{i=1}^N (p_i \cdot g_i)}{\sqrt{\sum_{i=1}^N p_i^2} \cdot \sqrt{\sum_{i=1}^N g_i^2}}$$

Here we calculate this metrics for all potential splits and when choose the best split wich minimizes the error.

