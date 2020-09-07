import scala.math.pow

object Solution {
  val (lowerbound, upperbound) = (-pow(2, 31), pow(2, 31)-1)
  val (lowerbound_divide_10, upperbound_divide_10) = (lowerbound/10, upperbound/10)

  def reverse(x: Int): Int = {
    var y: Int = x
    var res: Int = 0

    while(y != 0) {
      getNewRes(res, y) match {
        case Some(v) => res = v
        case None => return 0
      }
      y = y / 10
    }

    return res
  }

  def getNewRes(res: Int, y: Int): Option[Int] = {
    var nres: Int = res
    val mody: Int = y % 10

    if (lowerbound_divide_10 <= res &&
      res <= upperbound_divide_10) {
      nres *= 10
    } else {
      return None
    }

    if ((y >= 0 && nres <= upperbound - mody) ||
      (y <= 0 && lowerbound - mody <= nres)) {
      return Option[Int](nres + mody)
    }

    return None
  }
}