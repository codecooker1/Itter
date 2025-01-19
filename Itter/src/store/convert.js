var convert = {
    // (A) PROPERTIES
    reader : null, // file reader
    img : null, // selected image
  
    // (B) READ SELECTED IMAGE
    read : () => {
      convert.reader = new FileReader();
      convert.reader.onload = convert.obj;
      convert.reader.readAsDataURL(
        document.getElementById("cFile").files[0]
      );
      return false;
    },
  
    // (C) SELECTED IMAGE TO OBJECT
    obj : () => {
      convert.img = new Image();
      convert.img.onload = convert.go;
      convert.img.src = convert.reader.result;
    },
  
    // (D) CONVERT & DOWNLOAD
    go : () => {
      // (D1) CREATE EMPTY CANVAS
      let canvas = document.createElement("canvas"),
          ctx = canvas.getContext("2d");
  
      // (D2) DRAW IMAGE ONTO CANVAS
      canvas.width = convert.img.width;
      canvas.height = convert.img.height;
      ctx.drawImage(convert.img, 0, 0);
  
      // (D3) GET SELECTED IMAGE FORMAT
      let format = document.getElementById("cFormat").value,
          ext = format=="jpeg" ? "jpg" : format ;
  
      // (D4) CONVERT & "FORCE DOWNLOAD"
      let a = document.createElement("a");
      a.href = canvas.toDataURL(`image/${format}`);
      a.download = `converted.${ext}`;
      a.click();
      a.remove();
    }
  };