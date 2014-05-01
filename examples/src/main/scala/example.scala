
// When using lifted or direct embedding, slick generates the SQL from helpers in the 
// driver class loaded below
// not required if you're writing your own SQL queries
import scala.slick.driver.H2Driver.simple._

//Create a case class matching the database fields and types
case class User(username: String, id: Option[Long] = None)

case class UserProp(user_id: Long, bitcoins: Double = 0.0)

//define the database projection types
class Users(tag: Tag) extends Table[User](tag, "USERS"){
    def id = column[Option[Long]]("USER_ID", O.PrimaryKey, O.AutoInc)
    def username = column[String]("USERNAME")
    def * = (username, id) <> (User.tupled, User.unapply)
}

class UserProps(tag: Tag) extends Table[UserProp](tag, "USERPROPS"){
    def user_id = column[Long]("USER_ID")
    def bitcoins = column[Double]("BITCOINS")
    def * = (user_id, bitcoins) <> (UserProp.tupled, UserProp.unapply)
}

//magic
object Example extends App{
  Database.forURL("jdbc:h2:mem:test1", driver = "org.h2.Driver") withSession{ implicit session =>
    
  }
}
