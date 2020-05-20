function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function createMessageBlock(title, text) {
    const divBlock = document.createElement('div');
    divBlock.className = 'wrapper__auth';
    divBlock.id = "id_new_edit_block";
    divBlock.innerHTML = `<div class="auth__column_right"><div class="auth__column_right_form"><div class="auth__column_right_form__header">${ title }</div><div id="message_text"> ${ text }</div><div class="auth__column_right__form_footer"><label class="form_footer_button-submit"><input type="submit" form="auth_form" value="" style="display: none"><a href="#" id="login-submit-btn"><div class="auth__button_submit"  ><span>&#10004</span></div></a></label><label class="form_footer_button-cancel"><a href="#" id="cancel_btn"><div class="auth__button_submit" id="login-cancel-btn" ><span>&#9587</span></div></a></label></div></div></div>`;
    return divBlock;
}