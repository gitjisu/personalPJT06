1. User(AbstractUser) 커스텀하는게 처음에 어려웠는데 공식문서를 찾아가면서 수정 했고, 우리는 추가적으로 성별을 적을 수 있는 필드를 넣었다 -> 이부분을 select로 하면 좋을듯?

2. Movie는 User모델의 FK를 참조하고, Comment는 Movie와 User모두 참조해야 하는 부분에서 처음 접하는 모델필드라 어떻게 해야할지 막막했는데 페어님과 그냥 무작정 해보고 안되면 수정하고를 반복하다 보니 됐다! 그리고 함수에서 

   ```
           if form.is_valid():
               temp = form.save(commit=False)
               temp.user = request.user
               temp.save()
               return redirect('movies:index')
             
   ```

   commit=Fasle로 지정하고 하는 부분에서, 이해가 안가는 점들이 있었는데 페어님이 친절하게 설명 해 주셔서 이해가 됐음!

   ```
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.user = request.user
               comment.movie = movie
               comment.save()
   ```

   3. delete의 경우 작성자만 삭제할 수 있도록 하는 부분을 구현하는데

   ```
           if comment.user == request.user:
               comment.delete()   
               
           if request.user == movie.user:
               movie.delete()
   ```

   user_id나  username이 아닌 user로 사용하면 된다는 점도 배울 수 있었다.

   