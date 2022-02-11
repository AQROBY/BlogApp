from ..models.Post import Post

def seed(repo):
    post1 = Post(5, "Title", "This is the content", "ownerrr", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    post2 = Post(10, "This is an article", "Minimal Post", "Another owner", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tincidunt metus eu suscipit semper. Nulla fermentum imperdiet turpis, molestie egestas lacus. Proin hendrerit mattis venenatis. Cras nec libero sed purus molestie varius quis sed neque. Aenean mollis efficitur elit quis placerat. Fusce blandit, ligula nec sagittis sagittis, tortor diam tincidunt elit, non viverra tortor neque a purus. Donec commodo fringilla mattis. Nulla facilisi. Donec quis dui sed ligula auctor lacinia nec sit amet metus. Pellentesque sed nibh leo. Suspendisse sed vehicula eros. Phasellus fringilla, risus eget feugiat condimentum, ligula tortor sagittis lacus, et eleifend enim nisi ut felis. Curabitur consequat id enim vel maximus. Vivamus scelerisque urna nec dui ullamcorper dictum.\n\nNam vulputate tincidunt nisl venenatis feugiat. Nullam euismod pulvinar urna, a eleifend tellus euismod sed. Aliquam erat volutpat. Ut fermentum sollicitudin purus, sed placerat mauris condimentum vel. Donec sem nunc, auctor quis sapien sit amet, fermentum faucibus purus. Praesent molestie leo risus, in feugiat ligula porta non. Morbi ac est lacus. Nullam vel blandit sapien. In at nibh non ipsum efficitur pharetra et in metus. Donec non placerat est. Vivamus enim turpis, facilisis in luctus vitae, lobortis a massa. Etiam gravida, purus in dignissim pellentesque, purus lacus sollicitudin tellus, non dapibus arcu leo non eros. Aenean est velit, auctor vitae gravida aliquet, commodo ac mauris. In hac habitasse platea dictumst. Vivamus nec augue sit amet erat porta ultrices.\n\nVivamus vitae porttitor felis, nec pharetra ante. Nam dictum metus magna, id sodales neque rutrum nec. Nunc ac velit id ligula auctor eleifend. Donec id diam elit. Vestibulum enim quam, rhoncus nec pharetra id, eleifend quis dolor. Maecenas auctor enim magna, in posuere nulla lobortis sit amet. Donec vel eros in lectus commodo ornare. Donec at accumsan ex. Integer rutrum fringilla lacus vel accumsan. Etiam libero eros, elementum ac tortor eget, dignissim sagittis neque. Donec maximus, arcu vulputate dictum porttitor, sapien enim ornare metus, ut euismod lorem dui vitae libero.\n\nSed finibus finibus quam, non pretium augue vulputate ut. Mauris et felis tortor. Quisque vel velit at justo fringilla tincidunt. Curabitur sollicitudin mauris sit amet accumsan aliquam. Nunc aliquam enim massa, in semper ipsum pellentesque in. Ut volutpat convallis libero ut porta. Donec finibus elit mauris, consectetur eleifend arcu auctor in. Vestibulum diam ipsum, blandit id dictum sed, tincidunt ut magna. Sed at accumsan turpis, et aliquam nibh. Nulla imperdiet orci id sagittis gravida.\n\nEtiam eu eros eu leo finibus dignissim at non sem. Nullam diam tellus, cursus eu lacus vel, tincidunt porttitor lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus maximus, ligula quis pulvinar placerat, ipsum tortor condimentum sapien, sed efficitur purus sem eu nisi. Nulla facilisi. Mauris vel elit rutrum, rutrum nulla nec, efficitur ligula. Fusce sed lectus viverra felis mattis euismod id a massa. In hac habitasse platea dictumst. Quisque at dolor non nibh tempus rhoncus. Nunc tincidunt gravida nunc, ut maximus enim tincidunt eget. Vestibulum ut magna magna. In bibendum ullamcorper orci, vitae commodo odio malesuada sed."
    post3 = Post(1, "This is a seeded article", lorem, "Yet another owner", "2022-02-08 04:07:07", "2022-02-08 04:07:07")
    repo.create(post1)
    repo.create(post2)
    repo.create(post3)
    return repo