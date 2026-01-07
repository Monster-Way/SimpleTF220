### 链式求导法则
f'(x) = $\lim_{Δx \to a} \frac{f(x + Δx) - f(x)}{Δx}$

f'(g(x)) = $\lim_{Δx \to a} \frac{f(g(x + Δx)) - f(g(x))}{Δx}$
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = $\lim_{Δx \to a} \frac{f(g(x + Δx)) - f(g(x))}{Δx} * 1$
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = $\lim_{Δx \to a} \frac{f(g(x + Δx)) - f(g(x))}{Δx} * \frac{g(x + Δx) - g(x)}{g(x + Δx) - g(x)}$
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = $\lim_{Δx \to a} \frac{f(g(x + Δx)) - f(g(x))}{g(x + Δx) - g(x)} * \frac{g(x + Δx) - g(x)}{Δx}$
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = $\lim_{Δx \to a} \frac{f(h + Δh) - f(h)}{h + Δh - h} * g'(x)$
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = $f'(g(x)) * g'(x)$


$[f(g(x))]' = f'(g(x)) * g'(x)$

### 隐函数求导

