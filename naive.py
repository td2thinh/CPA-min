from math import sqrt
from typing import List

from Circle import Circle
from Point import Point


# Possible implementation of naive algorithm given by the professor
# SOURCE: https://www-npa.lip6.fr/~buixuan/cpa2023
def naiveAlgorithm(inputPoints: List["Point"]) -> "Circle":
    points = inputPoints.copy()
    if len(points) < 1:
        return None
    cX, cY, cRadiusSquared = None
    for p in points:
        for q in points:
            cX = 0.5 * (p.x + q.x)
            cY = 0.5 * (p.y + q.y)
            cRadiusSquared = 0.25 * (
                (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)
            )
            allHit = True
            for s in points:
                if (s.x - cX) * (s.x - cX) + (s.y - cY) * (s.y - cY) > cRadiusSquared:
                    allHit = False
                    break
            if allHit:
                return Circle(Point(cX, cY), sqrt(cRadiusSquared))

    resX = 0.0
    resY = 0.0
    resRadiusSquared = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                p = points[i]
                q = points[j]
                r = points[k]
                # si les trois sont colineaires on passe
                if (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x) == 0:
                    continue
                if (p.y == q.y) or (p.y == r.y):
                    if p.y == q.y:
                        p = points[
                            k
                        ]  # ici on est certain que p n'est sur la meme ligne de ni q ni r
                        r = points[i]  # parce que les trois points sont non-colineaires
                    else:
                        p = points[
                            j
                        ]  # ici on est certain que p n'est sur la meme ligne de ni q ni r
                        q = points[i]  # parce que les trois points sont non-colineaires
                # on cherche les coordonnees du cercle circonscrit du triangle pqr
                # soit m=(p+q)/2 et n=(p+r)/2
                mX = 0.5 * (p.x + q.x)
                mY = 0.5 * (p.y + q.y)
                nX = 0.5 * (p.x + r.x)
                nY = 0.5 * (p.y + r.y)
                # soit y=alpha1*x+beta1 l'equation de la droite passant par m et
                # perpendiculaire a la droite (pq)
                # soit y=alpha2*x+beta2 l'equation de la droite passant par n et
                # perpendiculaire a la droite (pr)
                alpha1 = (q.x - p.x) / (p.y - q.y)
                beta1 = mY - alpha1 * mX
                alpha2 = (r.x - p.x) / (p.y - r.y)
                beta2 = nY - alpha2 * nX
                # le centre c du cercle est alors le point d'intersection des deux droites
                # ci-dessus
                cX = (beta2 - beta1) / (alpha1 - alpha2)
                cY = alpha1 * cX + beta1
                cRadiusSquared = (p.x - cX) * (p.x - cX) + (p.y - cY) * (p.y - cY)
                if cRadiusSquared >= resRadiusSquared:
                    continue
                allHit = True
                for s in points:
                    if (s.x - cX) * (s.x - cX) + (s.y - cY) * (
                        s.y - cY
                    ) > cRadiusSquared:
                        allHit = False
                        break
                if allHit:
                    resX = cX
                    resY = cY
                    resRadiusSquared = cRadiusSquared

    return Circle(Point(resX, resY), sqrt(resRadiusSquared))


# -------------END OF CODE DU PROF---------------------------
