async function handler(event) {
    const request = event.request;
    const uri = request.uri;

    if (!uri.startsWith('/static/')) {
        request.uri = '/static/index.html';
    }

    return request;
}