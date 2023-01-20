# book-scrapper
I got the idea to learn web scraping from John Watson Rooney on YouTube, check out this link https://www.youtube.com/watch?v=p3Z-qtUp4p8.

The goal is gather some data about book catalog. I want to get the title, rating, price, stock availability, and image link.

I have been successful import the data into csv per page.

But still failed to import to_json because the output become appended from page 1 to page n + 1. My goal is make it save into json but perpage only and not appended into when the page increase.

Another goal is load the data into data lake (google cloud storage).

Need to learn about connection, credentials, and gcp command to migrate the data.
