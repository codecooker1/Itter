// import { createClient } from "@supabase/supabase-js"



export async function convertImage(imageFile) {
  console.log('Converting image...')
  const reader = new FileReader()
  reader.readAsDataURL(imageFile)

  await new Promise((resolve) => {
    reader.onload = () => {
      resolve()
    }
  })

  const img = new Image()
  img.src = reader.result

  await new Promise((resolve) => {
    img.onload = () => {
      resolve()
    }
  })

  const canvas = document.createElement('canvas')
  canvas.width = img.width
  canvas.height = img.height
  const ctx = canvas.getContext('2d')
  ctx.drawImage(img, 0, 0)
  const dataUrl = canvas.toDataURL('image/webp')
  const blob = await fetch(dataUrl).then(response => response.blob())
  const objectUrl = URL.createObjectURL(blob)
  console.log(`done converting image to webp: ${objectUrl}`)
  return blob
}


//Will complete later
// export async function uploadFile(file) {
//   const processedFile = await convertImage(file)
//   const media_url = ""

//   const { data, error } = await supabase.value.storage
//     .from('ItterMedia')
//     .upload(`/${authStore.user.username}/`, '' + nanoid(), processedFile, {contentType: processedFile.type})

//     if (error) {
//         console.error('Error uploading file:', error)
//         error.value = error
//     } else {
//       console.log('File uploaded successfully:', data)
//       media_url.value = await this.supabase.storage.from('profilepics').getPublicUrl(data.path).data.publicUrl
//       console.log('Public URL:', media_url.value)
//     }
// }