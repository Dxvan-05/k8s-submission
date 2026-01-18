const fs = require('fs')
const http = require('https')



const downloadNewImage = async (url, path) => {
    return new Promise((resolve, reject) => {
        http.get(url, (res) => {
            const { statusCode } = res

            if (statusCode === 302) {
                res.resume()
                resolve(downloadNewImage(res.headers.location, path))
                return
            }
            else if (statusCode == 200) {
                res.pipe(fs.createWriteStream(path))
                .on('error', () => reject('Image request: Could not write image to disk'))
                .on('close', () => resolve(path))
            } else {
                reject('Image Request: status code: ' + statusCode)
            }
            

            


        }).on('error', () => reject('Image request: Request failed'))
    })
}

module.exports = downloadNewImage
