$(() => {
    $('.signUpButton__T5rZ').on('click', () => {
        window.location.href = '/signup'
    })

    $('.loginButton__T5rZ').on('click', () => {
        window.location.href = '/login'
    })

    $('.submitSignUpFormButton__3cQN').on('click', (event) => {
        event.preventDefault();
    })
})