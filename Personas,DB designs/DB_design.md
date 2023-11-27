# Database Design Models:

## User Model:
- username
- bio
- profile_picture
- subcribers_count

## Video Model:
- title
- description
- uploaded_by (foreign key to User)
- uploaded_date
- video_file
- video_url (one of the above will be used)
- thumbnail
- views
- likes,dislikes
  
## Comment Model :
- user(foreign key to User)
- video(foreign key to Video)
- text
- created_time
- like,dislikes
  
## Subscriptions Model :
- subscriber(foreign key to user)
- subscribed_to(foreign key to user)

## Playlist Model :
- user
- title
- videos(many to many relation)
