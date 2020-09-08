import scala.collection.mutable._

object Solution {
  def orangesRotting(grid: Array[Array[Int]]): Int = {
    var q = Queue[Tuple2[Int, Int]]()
    var t = (0, 0)
    var res, x, y, oneLayerLen: Int = 0
    var rowLen = grid.length
    var colLen = grid(0).length
    var ngrid = grid
    var directions =  List((0, 1), (0, -1), (-1, 0), (1, 0))

    for(i<-0 until rowLen; j<-0 until colLen) {
      if (grid(i)(j) == 2) {
        q.enqueue((i, j))
      }
    }

    oneLayerLen = q.length
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

    for(i<-0 until rowLen; j<-0 until colLen) {
      if(ngrid(i)(j) == 1) {
        return -1
      }
    }

    return res
  }
}