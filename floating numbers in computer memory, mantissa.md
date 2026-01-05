---
type: note
status: done
tags: []
sources:
-
authors:
-
---

#⌛

Floating numbers space is continuous (and infinite), thus they can not be stored in memory without some loss of accuracy.

All numbers are written in a standardized IEEE-756 format, where each number is represented like:
$$\large (-1)^{sign}+Mantissa+2^{Exponent}$$

To make things clear, let's take some real number and convert it to the bit-representation.

**Step 1:** Convert number to binary base
$$\Large 7.25 \to 2^{2}+ 2^{1}+2^{0}+0^{-1}+2^{-2} \to 111.01_{2}$$

**Step 2:** Shift the decimal delimiter
All numbers have to has "1" as the integer part, so we shift the decimal delimiter to the left or to the right to get
$$\large 111.01_{2} \to 1.1101_{2}$$

All the rest of the numbers (".1101") are called the **Mantissa** and they are used to denote the decimal part of the value.

**Step 3:** Write down the exponent
Now we do calculate the number of shifts and assign that number to exponent. 

>[!quote] Note: 
>Shifts to the right are being counted with minus:
>$\large 0.00101 \to 1.01$ requires "$\large-3$" shift

$$\large 111.01_{2} = 1.1101_{2} \times 2^{2}$$

**Step 4:** Normalize the exponent
Notice, that exponents may be both positive and negative values, and we do not have a bit to store that sign. 

So, to determine which one is which, exponents are being normalized around 127 for 32-bit floats (as exponent can take 8 bits, so the greatest value is 255)

$$\large 1.1101_{2} \times 2^{2} \to 1.1101_{2} \times 2^{2 + 127 = 129}$$

**Step 5:** Write down the exponent in the binary base
$$\large 1.1101_{2} \times 2^{2 + 127 = 129} \to 1.1101_{2} \times 2^{10000001}$$

**Step 6:** Bring all parts together
$$\large \underbrace{0}_{\text{Sign bit}}\ |\ \underbrace{100000001}_{\text{Exponent (8 bits)}}\ |\ \underbrace{1101\ 0000\ 0000\ 0000\ 0000\ 0000}_{\text{Mantissa (23 bits)}} $$

## In context of machine learning
Modern Neural Networks (like LLMs) can have billions of parameters (weights), which takes a lot of memory to store and inference the model. 

So, floating numbers with smaller precisions are often used to train and inference neural networks. The popular formats are FP16, BF16, TF32, and even FP8.

The **quantization** is a trick when you do train a model using ordinary float32 values, for example, and then prune all the parameters to the lower precision, so the inference model becomes much smaller.