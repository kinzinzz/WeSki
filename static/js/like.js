// 좋아요 비동기 처리
const likeBtn = document.querySelector('#likeBtn')
likeBtn.addEventListener('click', function (event) {
    axios({
        method: 'GET',
        url: `/places/likes/${event.target.dataset.reviewId}/`
    })
        .then(response => {
            if (response.data.existed_user === true) {
                event.target.classList.add('fa-heart-fill')
                event.target.classList.remove('fa-heart')
            }
            else {
                event.target.classList.add('fa-heart')
                event.target.classList.remove('fa-heart-fill')

            }
            const likeCount = document.querySelector('#like-count')
            likeCount.innerText = response.data.likeCount
        })
})
