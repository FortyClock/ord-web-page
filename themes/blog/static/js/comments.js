(function () {
  const form = document.getElementById("pcs-comment-form");
  if (!form || !window.CommentSettings) return;

  const replyInput = document.getElementById("pcs-comment-form-input-replyto");
  const replyDisplay = document.getElementById("pcs-comment-form-display-replyto");

  window.CommentSystem = {
    setReply(slug, author) {
      const decodedSlug = decodeURIComponent(slug);
      const decodedAuthor = decodeURIComponent(author);
      replyInput.value = decodedSlug;
      replyDisplay.hidden = false;
      replyDisplay.innerHTML =
        '<button type="button" onclick="CommentSystem.cancelReply()">Отменить ответ</button>' +
        '<p>Ответ на комментарий автора <a href="#comment-' + decodedSlug + '">' + decodedAuthor + "</a>.</p>";
      form.scrollIntoView({ behavior: "smooth", block: "start" });
    },
    cancelReply() {
      replyInput.value = "";
      replyDisplay.hidden = true;
      replyDisplay.innerHTML = "";
    }
  };

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.getElementById("pcs-comment-form-input-name").value.trim();
    const website = document.getElementById("pcs-comment-form-input-website").value.trim();
    const text = document.getElementById("pcs-comment-form-input-textarea").value.trim();

    if (!name || !text) return;

    const settings = window.CommentSettings;
    const email = settings.emailUser + "@" + settings.emailDomain;
    const subject = "Комментарий к статье: " + settings.articleTitle;
    const lines = [
      "article: " + settings.articleSlug,
      "author: " + name,
      website ? "website: " + website : "",
      replyInput.value ? "replyto: " + replyInput.value : "",
      "",
      text
    ].filter(Boolean);

    window.location.href =
      "mailto:" + encodeURIComponent(email) +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(lines.join("\n"));
  });
})();
