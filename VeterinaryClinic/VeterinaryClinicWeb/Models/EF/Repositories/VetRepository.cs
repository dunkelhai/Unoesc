using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Models.EF.Repositories
{
    public class VetRepository : RepositoryBase<Vet>, IVetRepository
    {
        public VetRepository(BancoContext context) : base(context) { }
    }
}