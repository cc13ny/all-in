/*
 * Make the codes a bit modularized at the expense of performance
 * */

import scala.collection.mutable._

object Solution {
  def orangesRotting(grid: Array[Array[Int]]): Int = {
    val (rowLen, colLen) = (grid.length, grid(0).length)
    val directions =  Seq((0, 1), (0, -1), (-1, 0), (1, 0))

    var q = Queue(yieldRottenOrange(grid, rowLen, colLen): _*)
    var oneLayerLen = q.length
    var res, x, y: Int = 0
    var ngrid = grid
    var t = (0, 0)

    if (!q.isEmpty) res = -1

    while(!q.isEmpty) {
      t = q.dequeue
      oneLayerLen -= 1

      for((di, dj) <- directions) {
        x = di + t._1
        y = dj + t._2

        if (0 <= x && x < rowLen &&
          0 <= y && y < colLen &&
          ngrid(x)(y) == 1) {
          ngrid(x)(y) = 2
          q.enqueue((x, y))
        }
      }

      if(oneLayerLen == 0) {
        res += 1
        oneLayerLen = q.length
      }
    }

    if (existFreshOrange(grid)) -1 else res
  }

  def yieldRottenOrange(grid: Array[Array[Int]], rowLen: Int, colLen: Int) =
    // (0 until rowLen).flatMap(i => (0 until colLen).withFilter(j => grid(i)(j) == 2).map(j => (i, j)))
    for {
      i <- 0 until rowLen
      j <- 0 until colLen
      if grid(i)(j) == 2
    } yield (i, j)

  def existFreshOrange(grid: Array[Array[Int]]) =
    grid.exists(_.exists(_ == 1))
}