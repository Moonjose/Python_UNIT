particles = []
maxProbThreshold = 0.0
while maxProbThreshold < 1.0:
    tempParticle =  input('Digite o nome da particula: ')
    tempProbability = float(input('Digite a probabilidade dela ser detectada(ex: 0.4):  '))
    maxProbThreshold = maxProbThreshold + tempProbability
    maxProbThreshold = round(maxProbThreshold, 1)

    if (maxProbThreshold <= 1.0):
        particles.append({tempParticle, tempProbability})
    else: 
        maxProbThreshold = maxProbThreshold - tempProbability
        maxProbThreshold = round(maxProbThreshold, 1)

print(particles)