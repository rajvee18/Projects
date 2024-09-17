# Static method for linear regression

<font size="4">
    
Using calculus, you can determine the values of a and b that make the SSE a minimum. When you make the SSE a minimum, you have determined the points that are on the line of best fit. It turns out that the line of best fit has the equation:


<br>

$$
\hat{y}=a+bx$$
where,
$$
a=\hat{y}-b\hat{x}
$$
and
$$
b=\frac{\sum(x-\hat{x})(y-\hat{y})}{\sum(x-\hat{x})^2}
$$ 


<br>

## The Logistic model

Logistic model can be written as:

$$
\hat{y}=\sigma(x)=\frac{1}{1+\exp^{-(a+bx)}}
$$

<br>

<font size="4">
    
## The log loss is effective for logistic regression
$$
\mathscr{L}(y,\hat{y})=-\frac{1}{N}\bigg( \sum -y\log\hat{y}-(1-y)\log(1-\hat{y})\bigg)=-\frac{1}{N}\sum y\log\bigg(\frac{1}{1+\exp^{-a-bx}}\bigg)-\frac{1}{N}\sum(1-y)\log\bigg(1-\frac{1}{1+\exp^{-a-bx}}\bigg)
$$

$N$ being the number of data points and the sum is taken over all data points.

<br>

# Calculations for gradient descent
Now we calculate $\frac{\delta\mathscr{L}}{\delta b}$. Since $\mathscr{L}$ has two terms;
\
Calculating derivative for the first term:
$$
\frac{\delta}{\delta b}\exp^{-a-bx}=-x\exp^{-a-bx} \implies \frac{\delta}{\delta b} (1+\exp^{-a-bx})=-x\exp^{-a-bx}
$$
Then,
$$
\frac{\delta}{\delta b} (1+\exp^{-a-bx})^{-1}=-1(1+\exp^{-a-bx})^{-2} \frac{\delta}{\delta b}(1+\exp^{-a-bx})=-1(1+\exp^{-a-bx})^{-2}(-x\exp^{-a-bx})=\frac{x\exp^{-a-bx}}{(1+\exp^{-a-bx})^{2}}
$$
Then,
$$
\frac{\delta}{\delta b}\log\big((1+\exp^{-a-bx})^{-1}\big)=\frac{1}{(1+\exp^{-a-bx})^{-1})}\frac{\delta}{\delta b}(1+\exp^{-a-bx})^{-1}=\frac{b\exp^{-a-bx}(1+\exp^{-a-bx})}{(1+\exp^{-a-bx})^{2}}=\frac{x\exp^{-a-bx}}{(1+\exp^{-a-bx})}
$$
Then,
$$
\frac{\delta}{\delta b}\big(y\log((1+\exp^{-a-bx})^{-1})\big)=y\frac{\delta}{\delta b}\log\big((1+\exp^{-a-bx})^{-1}\big)=y\frac{x\exp^{-a-bx}}{(1+\exp^{-a-bx})}
$$
Then,
$$
\frac{\delta}{\delta b}-\sum\big(y\log((1+\exp^{-a-bx})^{-1})\big)=-\sum\frac{\delta}{\delta b}\big(y\log((1+\exp^{-a-bx})^{-1})\big)=-\sum y\frac{x\exp^{-a-bx}}{(1+\exp^{-a-bx})}
$$
\
Calculating derivative for the second term:
$$
\frac{\delta}{\delta b} (1+\exp^{-a-bx})^{-1}=\frac{x\exp^{-a-bx}}{(1+\exp^{-a-bx})^{2}}
$$
Then,
$$
\frac{\delta}{\delta b} (1-(1+\exp^{-a-bx})^{-1})=\frac{-x\exp^{-a-bx}}{(1+\exp^{-a-bx})^{2}}
$$
Then,
$$
\frac{\delta}{\delta b} \log(1-(1+\exp^{-a-bx})^{-1})=\frac{1}{1-\frac{1}{1+\exp^{-a-bx}}}\frac{\delta}{\delta b} (1-(1+\exp^{-a-bx})^{-1})=\frac{1}{1-\frac{1}{1+\exp^{-a-bx}}}\frac{-b\exp^{-a-bx}}{(1+\exp^{-a-bx})^{2}}=\frac{(1+\exp^{-a-bx})}{\exp^{-a-bx}}\frac{-b\exp^{-a-bx}}{(1+\exp^{-a-bx})^{2}}=\frac{-x}{1+\exp^{-a-bx}}
$$
Then,
$$
\frac{\delta}{\delta b} (1-y)\log(1-(1+\exp^{-a-bx})^{-1})=(1-y)\frac{-x}{1+\exp^{-a-bx}}
$$
Then,
$$
\frac{\delta}{\delta b} -\sum (1-y)\log(1-(1+\exp^{-a-bx})^{-1})=-\sum \frac{\delta}{\delta b} (1-y)\log(1-(1+\exp^{-a-bx})^{-1})= -\sum (1-y)\frac{-x}{1+\exp^{-a-bx}}
$$
\
Summing up the derivatives of the two terms we get
$$
\frac{\delta\mathscr{L}}{\delta b}=-\frac{1}{N}\sum\big(y\frac{x\exp^{-a-bx}}{1+\exp^{-a-bx}}+(1-y)\frac{-x}{1+\exp^{-a-bx}}\big)=-\frac{1}{N}\sum\frac{xy\exp^{-a-bx}+xy-x}{1+\exp^{-a-bx}}=-\frac{1}{N}\sum \big(xy - \frac{x}{1+\exp^{-a-bx}}\big)
$$
$$
=\frac{1}{N}\sum({x}(\hat{y}-y))
$$





