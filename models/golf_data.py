from models.golf import GolfModel
from models.comment import CommentModel
from models.category import CategoryModel


categories_list = [
    CategoryModel(name="golfclub_premium"),
    CategoryModel(name="golfclub_base"),
	CategoryModel(name="golfclub_mid")
]

golfs_list = [
  GolfModel(name="Golf Clubs and bag - Callaway", product_type_code="golfclubs", description="Callaway XR Irons 5,6,7,8,9", price=18, rating=4.9, in_stock=True, location="SE8 (London)", image="https://assets.fatllama.com/images/medium/golf-clubs-and-bag--callaway-46882136.jpg", categories=categories_list),
  GolfModel(name="Full set left handed golf clubs and bag / driver / putter", product_type_code="golfclubs", description="Full set of left handed Taylormade RAC golf clubs", price=24, rating=4.8, in_stock=True, location="N5 (London)", image="https://assets.fatllama.com/images/medium/full-set-left-handed-golf-clubs-and-bag--driver--putter-31851117.jpg", categories=categories_list),
  GolfModel(name="Golf Clubs QUALITY PING i3 irons W DRIVERS - RH", product_type_code="golfclubs", description="Ping I-3 irons, Odyssey putter and TaylorMade Burner Driver.", price=20, rating=4.7, in_stock=True, location="E2 (London)", image="https://assets.fatllama.com/images/medium/golf-clubs-quality-ping-i3-irons-w-drivers--rh-56589233.HEIC", categories=categories_list),
  GolfModel(name="Taylor Made golf clubs", product_type_code="golfclubs", description="Taylor Made r7 irons SW through to 4 iron, grips all in excellent condition.", price=20, rating=5.0, in_stock=True, location="SE22 (London)", image="https://assets.fatllama.com/images/medium/golf-club-set-13427939.jpg", categories=categories_list),
  GolfModel(name="Set of Titleist Golf Clubs with Bag", product_type_code="golfclubs", description="Set of Titleist Golf Clubs, with lightweight Titleist carry bag.", price=18, rating=5.0, in_stock=True, location="NW3 (London)", image="https://assets.fatllama.com/images/medium/set-of-titleist-golf-clubs-with-bag-72400016.jpg", categories=categories_list),
  GolfModel(name="Callaway Warbird Golf Clubs", product_type_code="golfclubs", description="Excellent condition, well looked after clubs.", price=20, rating=0, in_stock=True, location="HP18 (Aylesbury)", image="https://assets.fatllama.com/images/medium/callaway-warbird-golf-clubs--51956244.jpg", categories=categories_list)
]


comments_list = [
  CommentModel(content="great golfclubs", golf_id=1),
  CommentModel(content="useful and value for money", golf_id=2)
]

