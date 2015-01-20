/**
* haversine.js: contains necessary global functions needed to compute the distance
*               between two GPS coordinate points (longitude, latitude).
*/

/**
 * rad: converts degrees to radians.
 */
  var rad = function(x) {
    return x * Math.PI / 180;
  };

/**
 * getDistance: computes distance between two GPS coordinate points.
 *
 * @radius, earth's mean radius (m)
 * @a, haversine equation
 * @c, haversine equation
 * @d, haversine equation, distance between two GPS coordinate points (m)
 */
  var getDistance = function(p1, p2) {
    var radius = 6378137;
    var dLat = rad(p2.lat() - p1.lat());
    var dLong = rad(p2.lng() - p1.lng());
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(rad(p1.lat())) * Math.cos(rad(p2.lat())) *
      Math.sin(dLong / 2) * Math.sin(dLong / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = radius * c;
    return d;
  };
