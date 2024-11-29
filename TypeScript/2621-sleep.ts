async function sleep(millis: number): Promise<void> {
    return new Promise((resolve,reject)=>{
		setTimeout(() => {
			return resolve()
		}, millis);
	})
}


 
let t = Date.now()
sleep(100).then(() => console.log(Date.now() - t)) // 100
