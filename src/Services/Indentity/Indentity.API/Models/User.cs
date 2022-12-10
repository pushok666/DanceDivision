
namespace Indentity.API.Models;

public class User : IdentityUser
{
    public string Name { get; set; }
    public string Surname { get; set; }
    public string Username { get; set; }
    public int Age { get; set; }

    public User()
    {
        Name = string.Empty;
        Surname = string.Empty;
        Email = string.Empty;
        Username = string.Empty;
    }
}