factorize = (toFactorize) ->
  toFactorize = Number((toFactorize).toFixed(5))
  numeratorsFactors = []
  denominatorsFactors = []
  naturalNumber = 1
  while not ((toFactorize*naturalNumber)==parseInt(toFactorize*naturalNumber))
    naturalNumber++
  denominator = naturalNumber
  numerator = toFactorize * denominator
  return [numerator, denominator]

console.log factorize(10/9)

JITEurope = [1/1, 16/15, 9/8, 6/5, 5/4, ]