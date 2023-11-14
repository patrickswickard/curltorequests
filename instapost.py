class Instapost:
  def __init__(self):
    self.id = ''
    self.shortcode = ''
    self.width = 0
    self.height = 0
    self.display_url = ''
    self.tagged_user_list = []
    self.fact_check_overall_rating = ''
    self.fact_check_information = ''
    self.gating_info = ''
    self.sharing_friction_info = ''
    self.media_overlay_info = ''
    self.media_preview = ''
    self.userid = ''
    self.username = ''
    self.is_video = False
    self.has_upcoming_event = False
    self.accessibility_caption = ''
    self.tagged_user_list = []
    self.caption = ''
    self.location = ''
    self.sidecar_to_children_list = []

  def get_common_values(self,thisnode):
    self.id = thisnode.get('id','')
    self.shortcode = thisnode.get('shortcode','')
    #subfields
    height = ''
    width = ''
    dimensions = thisnode.get('dimensions',{})
    if dimensions:
      width = dimensions.get('width','')
      height = dimensions.get('height','')
    self.width = width
    self.height = height
    self.display_url = thisnode.get('display_url','')
    self.tagged_user_list = thisnode.get('edge_media_to_tagged_user',[])
    self.fact_check_overall_rating = thisnode.get('fact_check_overall_rating','')
    self.fact_check_information = thisnode.get('fact_check_information','')
    self.gating_info = thisnode.get('gating_info','')
    self.sharing_friction_info = thisnode.get('sharing_friction_info','')
    self.media_overlay_info = thisnode.get('media_overlay_info','')
    self.media_preview = thisnode.get('media_preview','')
    # subfields
    userid = ''
    username = ''
    owner = thisnode.get('owner',{})
    if owner:
      userid = owner.get('id','')
      username = owner.get('username','')
    self.userid = userid
    self.username = username
    self.is_video = thisnode.get('is_video',False)
    self.has_upcoming_event = thisnode.get('has_upcoming_event',False)
    self.accessibility_caption = thisnode.get('accessibility_caption','')

  def process_post(self,thispost):
    self.get_common_values(thispost)
    # after this point everything is attached only to the main post
    caption = ''
    if thispost.get('edge_media_to_caption',''):
      captionlist = thispost['edge_media_to_caption']['edges']
      if captionlist:
        caption = captionlist[0]
    self.caption = caption
    self.location = thispost.get('location','')
    # after this point these values only exist if we have subposts 
    my_sidecar_to_children_list = []
    sidecar_to_children = thispost.get('edge_sidecar_to_children',{})
    if sidecar_to_children:
      sidecar_to_children_list = sidecar_to_children.get('edges',[])
      if sidecar_to_children_list:
        for thissubpost in sidecar_to_children_list:
          thissubnode = thissubpost.get('node',{})
          if thissubnode:
            # create new post object
            mysubpost = Instapost()
            # grab the stuff only attached to main
            mysubpost.caption = self.caption
            mysubpost.location = self.location
            mysubpost.get_common_values(thissubnode)
            my_sidecar_to_children_list.append(mysubpost)
    self.sidecar_to_children_list = my_sidecar_to_children_list
