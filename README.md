# pyseeder
Generate and recreate data

# geo py

https://pypi.org/project/geo-py/

`def destination(point, distance, bearing):`

Given a start point, initial bearing, and distance, this will calculate the destina­tion point and final bearing travelling along a (shortest distance) great circle arc.

# formula

\begin{equation}
φ2 = asin( sin φ1 ⋅ cos δ + cos φ1 ⋅ sin δ ⋅ cos θ )
λ2 = λ1 + atan2( sin θ ⋅ sin δ ⋅ cos φ1, cos δ − sin φ1 ⋅ sin φ2 )
\end{equation}

where	φ is latitude, λ is longitude, θ is the bearing (clockwise from north), δ is the angular distance d/R; d being the distance travelled, R the earth’s radius
