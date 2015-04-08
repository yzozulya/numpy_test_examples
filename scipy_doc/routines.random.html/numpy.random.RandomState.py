import numpy as np

st = np.random.RandomState()

a = 1.
b = 2.
n = 1.
p = 1.
length = 1

df = 1
alpha = [1, 2, 3]

st.beta(a, b)
st.binomial(n, p)
st.bytes(length)
st.chisquare(df)
st.choice(a)
st.dirichlet(alpha)
st.exponential()
dfnum = 1
dfden = 1

st.f(dfnum, dfden)

shape = (1, 2)
st.gamma(shape)
st.geometric(p)
st.get_state()
st.gumbel()

ngood = 1
nbad = 1
nsample = 2

st.hypergeometric(ngood, nbad, nsample)
st.st.laplace()
st.st.logistic()
st.lognormal()
st.logseries(p)

n = 1
pvals = [1, 2]

st.multinomial(n, pvals)

mean = 1
cov = 1

st.multivariate_normal(mean, cov)
st.negative_binomial(n, p)

nonc = 1

st.noncentral_chisquare(df, nonc)
st.noncentral_f(dfnum, dfden, nonc)
st.normal()
st.pareto(a)

x = 1
st.permutation(x)
st.poisson()
st.power(a)
st.rand(1, 2, 3)

low = 1

st.randint(low)
st.randn(1, 2, 3)
st.random_integers(low)
st.random_sample()
st.rayleigh()
st.seed()

state = 1
st.set_state(state)

x = [1, 2, 3]
st.shuffle(x)
st.standard_cauchy()
st.standard_exponential()

shape = 1.
st.standard_gamma(shape)
st.standard_normal()
st.standard_t(df)
st.tomaxint()
st.triangular(1, 2, 3)
st.uniform()

mu = 1
kappa = 1
st.vonmises(mu, kappa)

scale = 1
st.wald(mean, scale)
st.weibull(a)
st.zipf(a)