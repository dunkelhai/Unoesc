using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class ProcedureController : Controller
    {
        private readonly IProcedureRepository _procedureRepository;

        public ProcedureController(IProcedureRepository procedureRepository) =>
            _procedureRepository = procedureRepository;

        // GET: Procedure
        public async Task<IActionResult> Index() =>
            View(await _procedureRepository.GetAll());

        // GET: Procedure/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _procedureRepository.GetById(id) is Procedure procedure)
                return View(procedure);

            return NotFound();
        }

        // GET: Procedure/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Procedure/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,ProcedureName,Observation")] Procedure procedure)
        {
            ModelState.Remove(nameof(procedure.Attendances));
            if (ModelState.IsValid)
            {
                await _procedureRepository.Add(procedure);
                return RedirectToAction(nameof(Index));
            }
            return View(procedure);
        }

        // GET: Procedure/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _procedureRepository.GetById(id) is Procedure procedure)
                return View(procedure);

            return NotFound();
        }

        // POST: Procedure/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,ProcedureName,Observation")] Procedure procedure)
        {
            if (id != procedure.Id)            
                return NotFound();

            ModelState.Remove(nameof(procedure.Attendances));
            if (ModelState.IsValid)
            {
                try
                {
                    await _procedureRepository.Update(procedure);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }
            return View(procedure);
        }

        // GET: Procedure/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _procedureRepository.GetById(id) is Procedure procedure)
                return View(procedure);

            return NotFound();
        }

        // POST: Procedure/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _procedureRepository.GetById(id) is Procedure procedure)
                await _procedureRepository.Delete(procedure);

            return RedirectToAction(nameof(Index));
        }
    }
}
