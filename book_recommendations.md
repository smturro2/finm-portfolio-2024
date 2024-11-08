# References: Portfolio Theory

## Intro Books

### Bodie, Kane, Marcus. *Investments* (2018)

Intro reference text to finance, widely used at the masters and advanced undergraduate levels.

**Core material:**

- Chapters 7-10 cover diversification, mean-variance optimization, and Linear Factor Pricing Models.
- Chapter 5 covers basics of returns and risk.
- Chapter 24 covers performance evaluation.

**Extra material:**

- Chapters 2-4 are a good introduction to securities, asset classes, and financial institutions.

### Pedersen. *Efficiently Inefficient* (2015)

This book reads easily. It is not a reference textbook as much as a tour of investing to give context. It is a fairly brief and non-technical introduction to various aspects of institutional investing. I'd say it is an "intro" book for a "quant" audience. Unlike some other books in this category, it is not a broad book for undergrads.

- The introduction and Chapter 1 are a helpful introduction to institutional investing and markets. 
- It also has good coverage of the concept of market efficiency and rationality.
- Other chapters give a light tour of important concepts for a quant.

### Paleologo. *Advanced Portfolio Management* (2021)

The name is misleading; it is "advanced" only for fundamental analysts new to quant. I include it here for having some good discussion of the concepts of portfolio management. It is an easy read that can help you build context for the more technical and advanced work.

## Quant Books

### Isichenko. *Quantitative Portfolio Management* (2021)

Strong applied focus, much more so than most textbooks. Nearly half the book is Chapter 2 which covers models for forecasting, including many machine-learning approaches. This book gets into technical topics at a serious level, but not a thorough level. It may be a strong way to get acquainted with models (and some empirical results) relevant for industry quants. Then, to get deeper in those models, you will need additional resources.

An additional reason I list this book is that it has a lot of value while also being very short and easy to read. Thus, it is highly suited to new quants.

- Unusually, it has an interview question at the start of every subsection.

### Paleologo. *Elements of Quantitative Investing* (2025)

Like Isichenko, the author has deep experience in industry, and it shows in the tone and coverage of the book. In terms of coverage, this book is one of the most closely related to this course. It is scheduled to be published in 2025, but a draft is available at the author's website.

### Hull. *Options Futures, and Other Derivatives* (2018)

The standard reference for options, but has a few good pieces for Portfolio. Advanced enough for grad studies, but more practical/applied than most Ph.D. references.

**Core material:**

- Chapter 22 - Value-at-Risk and tail-risk measures. Good treatment of using Monte Carlo and PCA for VaR, which is also useful intro to using those methods more generally.
- Chapter 23 - Volatility models. EWMA and GARCH are the main features.

### Chincarini and Kim. *Quantitative Equity Portfolio Management* (2022)

This book may be the best representative of the FINM 36700 course in terms of its scope of topics and balance of financial math versus discussion of application.

### Antti Ilmanen. *Expected Returns* (2011)

Textbook with unique angle as being extremely applied while discussing serious quant topics.

**Core material:**

- Part II - A Dozen Case Studies (Chapters 8-19)
- Nice introduction to key (quant-relevant) issues across various asset classes.

**Other material:**

- Part I (chapters 1-7) have good discussions of how to think about expected returns, whether they are rational vs behavioral, etc. (The discussion of the history of returns is a bit dated, but still a good intro.)
- Chapter 24 has good practical advice on how to build a forecasting model.

### Meucci. *Risk and Asset Allocation* (2007)

Mathematical treatment (little empirical focus) on:

- Part 1: Stats of returns
- Part 2: Classic allocation (including MV in Chapter 6.)
- Part 3: Bayesian perspective and Black Litterman (Ch. 9)

## Books for Academic Research

This is useful for understanding research and theoretical foundations. But it is not so applied/practical to be of high interest for most practitioners.

### Campbell. *Financial Decisions and Markets* (2018)

This book is more recent and has a good survey of where research is developing on each issue. If you're looking for an entry into research, I'd start here.

### Cochrane. *Asset Pricing* (2005)

This book is the classic Ph.D. level treatment of the theory, with all the derivations and a strong framing via the Stochastic Discount Factor. If looking for Ph.D. level focus on the theoretical modeling, I'd start here.

# References: Regression

## Foundations

### Hayashi, Fumio - *Econometrics* (2000)

Graduate level, nice blend of theory and application. Most importantly, Princeton Press puts the first chapter online for free.

**Highlight:**

- Chapter 1 is a strong introduction to classic OLS.
- Also a very good discussion of why strict exogeneity is not satisfied in lagged time-series regressions.
- For the future: Has a strong chapter on non-stationary time-series data.

**Warning:**

- As a comprehensive graduate reference, it gets into many topics we will not use.

### Cunningham, Scott (2021) - *Causal Inference*

Somewhat quirky book on regression for applied microeconomics. The publisher puts the entire book online for free.

**Highlight:**

- Chapter 2 has a very intuitive discussion of probability and OLS. Includes Python code.

**Warning:**

- Most of the rest of the book is not a priority for quant finance. Stick with Chapter 2.

### Lin, Timothy (2018) - *Notes on Regression*

Six-part series of online notes showing that OLS regression can be derived and interpreted in many ways.

- Link to Part 6. (At the start of the note, links to the first 5 are given.)

### StackOverflow & CodeAcademy (2021) - *Linear Regression for Python*

Series of free videos.

**Note:**

- Posting this as example of the many(!) OLS in Python tutorials out there.
- I am not sure if this one is particularly strong compared to what else you might find, so look around.
- If you find one you like more, tell me!
- This series is hosted on StackOverflow, and does a good job of linking to relevant questions covered in the videos.

## Other Resources

### Wooldridge, Jeffrey (2019) - *Introductory Econometrics: A Modern Approach*

Classic undergraduate intro to regression.

**Highlight:**

- Chapters 2-5 are a very strong textbook introduction to OLS.
- Similarly, Chapters 10-12 are a nice intro to issues with time series data in OLS.

### Wooldridge, Jeffrey (2010) - *Econometric Analysis of Cross Section and Panel Data*

Very theoretical, graduate level. Considered a/the principal reference for econometrics used in microeconomics.

**Highlight:**

- Chapter 2. OLS as an estimator of the conditional expectation.
- For the future: Chapter 8 on GMM, relating it to OLS. Chapter 13 on MLE.

**Warning:**

- Much of the focus is on methods used in microeconomics that see little use in finance. (Such as Sections II and III).