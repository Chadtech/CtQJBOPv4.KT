window.AudioContext = window.AudioContext or window.webkitAudioContext
context = new AudioContext()

oscillators = []

oscillators.forEach (element)->
  element.connect(context.destination)

tones= [1/1, 9/8, 5/4, 4/3, 3/2, 5/3, 15/8, 2/1]

#aMajor = [1/1, 9/8, 32/25, 27/20, 3/2, 27/16, 48/25, ]

rows = [
  [49, 50, 51, 52, 53, 54, 55, 56],
  [81, 87, 69, 82, 84, 89, 85, 73],
  [65, 83, 68, 70, 71, 72, 74, 75],
  [90, 88, 67, 86, 66, 78, 77, 188]
  ]

$(document).ready ()->
  $('body').keydown (event)->
    proceed = true
    oscillatorIndex = 0
    while oscillatorIndex < oscillators.length
      if oscillators[oscillatorIndex][0]==event.which
        proceed= false
      oscillatorIndex++
    if proceed
      rowSuspect = 0
      while rowSuspect<rows.length
        keySuspect = 0
        while keySuspect<rows[rowSuspect].length
          if rows[rowSuspect][keySuspect]==event.which
            newOscillator = context.createOscillator()
            newVolume = context.createGain()
            newOscillator.connect(newVolume)
            newVolume.connect(context.destination)
            newVolume.gain.value = 0.3
            newOscillator.frequency.value = 50*(tones[keySuspect])*Math.pow(2,rowSuspect)
            newOscillator.start(0)
            oscillators.push [event.which, newVolume]
          keySuspect++
        rowSuspect++

$(document).ready ()->
  $('body').keyup (event)->
    oscillatorIndex = 0
    while oscillatorIndex < oscillators.length
      if oscillators[oscillatorIndex][0]==event.which
        oscillators[oscillatorIndex][1].disconnect()
        oscillators.splice(oscillatorIndex,1)
      oscillatorIndex++